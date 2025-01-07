# Log Archive Tool

Project URL:   https://roadmap.sh/projects/log-archive-tool


A command-line tool to archive log files by compressing them into a dated tar.gz archive. This tool helps maintain system cleanliness while preserving logs for future reference.

## Features

- Archives logs from any specified directory
- Creates compressed tar.gz archives with timestamp
- Maintains an archive history log
- Provides archive details (size, number of files)
- Validates input directory and permissions
- Creates dated archive names automatically

## Requirements

- Unix-like operating system (Linux, macOS)
- Bash shell
- tar command-line utility (usually pre-installed)

## Installation

1. Download the script:
```bash
curl -O https://github.com/trxngxx/ROADMAP-SH.git
# or
wget https://github.com/trxngxx/ROADMAP-SH.git
```

2. Make it executable:
```bash
chmod +x log-archive
```

3. Optionally, move to system path:
```bash
sudo mv log-archive /usr/local/bin/
```

## Usage

Basic usage:
```bash
./log-archive <log-directory>
```

Example:
```bash
./log-archive /var/log
```

This will:
1. Create an archive directory named `archived_logs` in the current directory
2. Compress all files from the specified directory
3. Name the archive with current timestamp (e.g., `logs_archive_20240107_123456.tar.gz`)
4. Log the operation to `archive_history.log`

## Output Example

```
Creating archive from /var/log...
Successfully created archive: ./archived_logs/logs_archive_20240107_123456.tar.gz

Archive details:
Location: ./archived_logs/logs_archive_20240107_123456.tar.gz
Size: 15M
Files included: 47
```

## Directory Structure

After running the tool:
```
./archived_logs/
├── logs_archive_20240107_123456.tar.gz
├── logs_archive_20240107_234567.tar.gz
└── archive_history.log
```

## Error Handling

The script handles various error conditions:
- Missing directory argument
- Non-existent directory
- Permission issues
- Archive creation failures

## Logging

The tool maintains an archive history log (`archive_history.log`) containing:
- Date and time of archive creation
- Source directory
- Archive filename

## Customization

You can modify the script to:
- Change the archive directory location
- Modify the archive naming format
- Add additional compression options
- Include/exclude specific file patterns

## Troubleshooting

Common issues and solutions:

1. **Permission Denied**
   ```bash
   Error: Cannot read directory '/var/log'. Please check permissions
   ```
   Solution: Run with sudo or ensure proper permissions
   ```bash
   sudo ./log-archive /var/log
   ```

2. **Directory Not Found**
   ```bash
   Error: Directory '/path/to/logs' does not exist
   ```
   Solution: Verify the directory path exists

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Your Name]
[Your Contact Information]

## Acknowledgments

- Inspired by Unix system administration needs
- Thanks to the Unix/Linux community for robust command-line tools