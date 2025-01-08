import hashlib
import os
import json
import argparse
import logging
from typing import Dict, List, Tuple
from datetime import datetime

class FileIntegrityChecker:
    def __init__(self, hash_file: str = "hashes.json"):
        self.hash_file = hash_file
        # Thiết lập logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('integrity_checker.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def calculate_hash(self, file_path: str) -> str:
        """Tính toán SHA-256 hash của file"""
        try:
            sha256_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except (IOError, PermissionError) as e:
            self.logger.error(f"Không thể đọc file {file_path}: {str(e)}")
            return None

    def store_hashes(self, path: str) -> None:
    # Thêm backup trước khi ghi file mới
    if os.path.exists(self.hash_file):
        backup_file = f"{self.hash_file}.bak"
        try:
            os.replace(self.hash_file, backup_file)
            self.logger.info(f"Backup created: {backup_file}")
        except OSError as e:
            self.logger.warning(f"Could not create backup: {str(e)}")

        hashes = {}
        if os.path.isfile(path):
            hash_value = self.calculate_hash(path)
            if hash_value:
                hashes[path] = hash_value
        else:
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    hash_value = self.calculate_hash(file_path)
                    if hash_value:
                        hashes[file_path] = hash_value

        try:
            with open(self.hash_file, "w") as f:
                json.dump(hashes, f, indent=4)
            self.logger.info("Hashes stored successfully.")
        except IOError as e:
            self.logger.error(f"Không thể lưu file hash: {str(e)}")

    def check_integrity(self, path: str, report_file: str = None) -> List[Tuple[str, bool]]:
        """Kiểm tra tính toàn vẹn của file/thư mục"""
        results = []
        try:
            if not os.path.exists(self.hash_file):
                self.logger.error("File hash chưa được khởi tạo")
                return results

            with open(self.hash_file, "r") as f:
                stored_hashes = json.load(f)
        except IOError as e:
            self.logger.error(f"Không thể đọc file hash: {str(e)}")
            return results

        if os.path.isfile(path):
            current_hash = self.calculate_hash(path)
            is_modified = current_hash != stored_hashes.get(path)
            results.append((path, is_modified))
        else:
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file_path in stored_hashes:
                        current_hash = self.calculate_hash(file_path)
                        is_modified = current_hash != stored_hashes[file_path]
                        results.append((file_path, is_modified))
                        
        # Xuất báo cáo n�u được yêu cầu
        if report_file:
            self._generate_report(results, report_file)

        return results

    def _generate_report(self, results: List[Tuple[str, bool]], report_file: str) -> None:
        """Tạo báo cáo kiểm tra"""
        try:
            with open(report_file, 'w') as f:
                f.write(f"File Integrity Check Report - {datetime.now()}\n")
                f.write("-" * 50 + "\n\n")
                for path, is_modified in results:
                    status = "Modified" if is_modified else "Unmodified"
                    f.write(f"Status: {status} - {path}\n")
            self.logger.info(f"Báo cáo đã được lưu tại: {report_file}")
        except IOError as e:
            self.logger.error(f"Không thể tạo file báo cáo: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("command", choices=["init", "check", "update"],
                       help="Command to execute")
    parser.add_argument("path", help="File or directory path")
    parser.add_argument("--report", help="Output report file path")
    args = parser.parse_args()

    checker = FileIntegrityChecker()

    try:
        if args.command == "init":
            checker.store_hashes(args.path)
        elif args.command == "check":
            results = checker.check_integrity(args.path, args.report)
            for path, is_modified in results:
                status = "Modified" if is_modified else "Unmodified"
                print(f"Status: {status} - {path}")
        elif args.command == "update":
            checker.store_hashes(args.path)
    except Exception as e:
        logging.error(f"Lỗi không mong đợi: {str(e)}")
        raise

if __name__ == "__main__":
    main()