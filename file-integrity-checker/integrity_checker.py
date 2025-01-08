import hashlib
import os
import json
import argparse
import logging
from typing import Dict, List, Optional
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

class FileIntegrityChecker:
    def __init__(self, hash_file: str = "hashes.json"):
        self.hash_file = hash_file
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Thiết lập logging với file và console output"""
        log_format = '%(asctime)s - %(levelname)s - %(message)s'
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[
                logging.FileHandler('integrity_checker.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def calculate_hash(self, file_path: str) -> Optional[Dict]:
        """Tính toán hash và metadata của file"""
        try:
            file_path = Path(file_path)
            if not file_path.is_file():
                self.logger.error(f"Không tìm thấy file: {file_path}")
                return None

            sha256_hash = hashlib.sha256()
            file_stat = file_path.stat()
            
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)

            return {
                "hash": sha256_hash.hexdigest(),
                "size": file_stat.st_size,
                "modified_time": datetime.fromtimestamp(file_stat.st_mtime).isoformat(),
                "checked_time": datetime.now().isoformat(),
                "path": str(file_path)
            }
        except (IOError, PermissionError) as e:
            self.logger.error(f"Lỗi khi đọc file {file_path}: {str(e)}")
            return None

    def _create_backup(self) -> bool:
        """Tạo backup cho file hash hiện tại"""
        if not Path(self.hash_file).exists():
            return True

        backup_file = f"{self.hash_file}.bak"
        try:
            os.replace(self.hash_file, backup_file)
            self.logger.info(f"Đã tạo backup tại: {backup_file}")
            return True
        except OSError as e:
            self.logger.error(f"Không thể tạo backup: {str(e)}")
            return False

    def store_hashes(self, path: str) -> None:
        """Lưu trữ hash của file hoặc các file trong thư mục"""
        path = Path(path)
        if not path.exists():
            self.logger.error(f"Đường dẫn không tồn tại: {path}")
            return

        # Tạo backup trước khi cập nhật
        if not self._create_backup():
            return

        hashes = {}
        if path.is_file():
            hash_data = self.calculate_hash(str(path))
            if hash_data:
                hashes[str(path)] = hash_data
        else:
            files_to_hash = [str(f) for f in path.rglob('*') if f.is_file()]
            
            with ThreadPoolExecutor() as executor:
                future_to_file = {
                    executor.submit(self.calculate_hash, file_path): file_path 
                    for file_path in files_to_hash
                }
                
                for future in as_completed(future_to_file):
                    file_path = future_to_file[future]
                    try:
                        hash_data = future.result()
                        if hash_data:
                            hashes[file_path] = hash_data
                    except Exception as e:
                        self.logger.error(f"Lỗi khi tính hash cho {file_path}: {str(e)}")

        try:
            with open(self.hash_file, "w") as f:
                json.dump(hashes, f, indent=4)
            self.logger.info("Lưu hash thành công")
        except IOError as e:
            self.logger.error(f"Không thể lưu file hash: {str(e)}")

    def compare_file_details(self, file_path: str, stored_data: Dict) -> Optional[Dict]:
        """So sánh chi tiết file với dữ liệu đã lưu"""
        current_data = self.calculate_hash(file_path)
        if not current_data:
            return None

        return {
            "path": file_path,
            "is_modified": current_data["hash"] != stored_data["hash"],
            "size_changed": current_data["size"] != stored_data["size"],
            "modification_time_changed": current_data["modified_time"] != stored_data["modified_time"],
            "current_data": current_data,
            "stored_data": stored_data
        }

    def check_integrity(self, path: str, report_file: str = None) -> List[Dict]:
        """Kiểm tra tính toàn vẹn của file/thư mục"""
        path = Path(path)
        results = []

        try:
            if not Path(self.hash_file).exists():
                self.logger.error("File hash chưa được khởi tạo")
                return results

            with open(self.hash_file, "r") as f:
                stored_hashes = json.load(f)
        except IOError as e:
            self.logger.error(f"Không thể đọc file hash: {str(e)}")
            return results

        if path.is_file():
            if str(path) in stored_hashes:
                result = self.compare_file_details(str(path), stored_hashes[str(path)])
                if result:
                    results.append(result)
        else:
            for file_path in path.rglob('*'):
                if str(file_path) in stored_hashes:
                    result = self.compare_file_details(
                        str(file_path), 
                        stored_hashes[str(file_path)]
                    )
                    if result:
                        results.append(result)

        if report_file:
            self._generate_report(results, report_file)

        return results

    def _generate_report(self, results: List[Dict], report_file: str) -> None:
        """Tạo báo cáo chi tiết"""
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write("File Integrity Check Report\n")
                f.write(f"Generated: {datetime.now().isoformat()}\n")
                f.write("-" * 50 + "\n\n")

                modified_files = [r for r in results if r["is_modified"]]
                f.write(f"Tổng số file kiểm tra: {len(results)}\n")
                f.write(f"Số file đã thay đổi: {len(modified_files)}\n\n")

                for result in results:
                    f.write(f"File: {result['path']}\n")
                    f.write(f"Trạng thái: {'Đã sửa đổi' if result['is_modified'] else 'Không thay đổi'}\n")
                    
                    if result["is_modified"]:
                        f.write("Chi tiết thay đổi:\n")
                        if result["size_changed"]:
                            f.write(f"  - Kích thước: {result['stored_data']['size']} -> {result['current_data']['size']} bytes\n")
                        if result["modification_time_changed"]:
                            f.write(f"  - Thời gian sửa đổi: {result['stored_data']['modified_time']} -> {result['current_data']['modified_time']}\n")
                        f.write(f"  - Hash cũ: {result['stored_data']['hash']}\n")
                        f.write(f"  - Hash mới: {result['current_data']['hash']}\n")
                    f.write("\n")

            self.logger.info(f"Đã tạo báo cáo tại: {report_file}")
        except IOError as e:
            self.logger.error(f"Không thể tạo file báo cáo: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("command", choices=["init", "check", "update"],
                       help="Lệnh thực thi (init/check/update)")
    parser.add_argument("path", help="Đường dẫn đến file hoặc thư mục")
    parser.add_argument("--report", help="Đường dẫn file báo cáo đầu ra")
    parser.add_argument("--hash-file", default="hashes.json",
                       help="File lưu trữ hash (mặc định: hashes.json)")
    args = parser.parse_args()

    checker = FileIntegrityChecker(hash_file=args.hash_file)

    try:
        if args.command == "init":
            checker.store_hashes(args.path)
        elif args.command == "check":
            results = checker.check_integrity(args.path, args.report)
            if not args.report:  # In kết quả ra console nếu không có file báo cáo
                for result in results:
                    status = "Đã sửa đổi" if result["is_modified"] else "Không thay đổi"
                    print(f"Trạng thái: {status} - {result['path']}")
        elif args.command == "update":
            checker.store_hashes(args.path)
    except Exception as e:
        logging.error(f"Lỗi không mong đợi: {str(e)}")
        raise

if __name__ == "__main__":
    main()