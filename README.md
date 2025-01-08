# File Integrity Checker

Project URL: https://roadmap.sh/projects/file-integrity-checker

A robust Python tool for monitoring and verifying file integrity using SHA-256 hashing. This tool helps detect unauthorized modifications to files and directories by maintaining and comparing hash signatures.

## Features

- SHA-256 hash calculation for files
- Support for both single files and directories
- Multi-threaded processing for improved performance
- Detailed change detection (size, modification time, hash)
- Automatic backup of hash database
- Comprehensive logging
- Detailed report generation
- UTF-8 support for file handling

## Requirements

- Python 3.7 or higher
- Required Python packages:
  ```
  pathlib
  typing
  concurrent.futures
  ```

## Installation

1. Clone or download the repository:
   ```bash
   git clone https://github.com/trxngxx/ROADMAP-SH.git
   cd file-integrity-checker
   ```

2. Make sure you have all required packages installed:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The tool provides three main commands: `init`, `check`, and `update`.

### Basic Commands

1. Initialize hash database for files/directories:
   ```bash
   python integrity_checker.py init /path/to/monitor
   ```

2. Check file integrity:
   ```bash
   python integrity_checker.py check /path/to/check
   ```

3. Update hash database:
   ```bash
   python integrity_checker.py update /path/to/update
   ```

### Advanced Options

- Generate a detailed report:
  ```bash
  python integrity_checker.py check /path/to/check --report report.txt
  ```

- Use custom hash database file:
  ```bash
  python integrity_checker.py init /path/to/monitor --hash-file custom_hashes.json
  ```

## Common Use Cases

### 1. Monitoring System Files

```bash
# Initialize monitoring for system log directory
python integrity_checker.py init /var/log

# Periodically check for changes
python integrity_checker.py check /var/log --report system_logs_report.txt
```

### 2. Securing Configuration Files

```bash
# Monitor configuration directory
python integrity_checker.py init /etc/myapp/config
python integrity_checker.py check /etc/myapp/config
```

### 3. Tracking Multiple Directories

```bash
# Initialize separate hash databases for different directories
python integrity_checker.py init /path1 --hash-file hashes1.json
python integrity_checker.py init /path2 --hash-file hashes2.json

# Check each directory separately
python integrity_checker.py check /path1 --hash-file hashes1.json
python integrity_checker.py check /path2 --hash-file hashes2.json
```

### 4. Automated Monitoring Script Example

```bash
#!/bin/bash
MONITOR_DIR="/important/files"
REPORT_DIR="/var/log/integrity_reports"
DATE=$(date +%Y%m%d_%H%M%S)

python integrity_checker.py check $MONITOR_DIR \
  --report "$REPORT_DIR/report_$DATE.txt"
```

## Output Examples

### Console Output
```
Status: Modified - /path/to/file1.txt
Status: Unmodified - /path/to/file2.txt
Status: Modified - /path/to/file3.conf
```

### Report File Content Example
```
File Integrity Check Report
Generated: 2025-01-08T14:30:45.123456

Total files checked: 3
Modified files: 2

File: /path/to/file1.txt
Status: Modified
Changes detected:
  - Size: 1024 -> 1536 bytes
  - Modification time: 2025-01-08T12:00:00 -> 2025-01-08T14:25:30
  - Old hash: a1b2c3d4...
  - New hash: e5f6g7h8...

File: /path/to/file2.txt
Status: Unmodified
```

## Logging

The tool maintains a log file (`integrity_checker.log`) with detailed information about all operations:
- File access errors
- Hash calculation status
- Backup operations
- General execution flow

## Error Handling

The tool handles various error scenarios:
- Invalid paths
- Permission issues
- File read/write errors
- Hash database corruption

Each error is logged with appropriate context for troubleshooting.

## Best Practices

1. Regular Monitoring
   - Set up scheduled checks using cron jobs
   - Keep reports for audit trails
   - Monitor the log file for errors

2. Hash Database Management
   - Keep backups of hash databases
   - Update hashes after legitimate changes
   - Use separate hash files for different security domains

3. Security Considerations
   - Store hash databases in secure locations
   - Restrict access to the tool and hash files
   - Validate hash database integrity regularly

## Troubleshooting

### Common Issues and Solutions

1. Permission Denied
   ```bash
   sudo chown user:group integrity_checker.py
   chmod +x integrity_checker.py
   ```

2. Hash Database Corrupted
   ```bash
   # Restore from backup
   cp hashes.json.bak hashes.json
   ```

3. High CPU Usage
   - Monitor large directories in smaller chunks
   - Schedule checks during off-peak hours

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.