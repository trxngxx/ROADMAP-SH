# Server Statistics Script

A Bash script that provides comprehensive server performance statistics for Linux systems. This script collects and displays various system metrics including CPU usage, memory utilization, disk space, and process information.

## Features

- **CPU Usage Statistics**
  - Total CPU usage percentage
  - Current system load

- **Memory Usage Information**
  - Total available memory
  - Used memory (with percentage)
  - Free memory (with percentage)
  - Buffer/Cache usage

- **Disk Usage Details**
  - Partition information
  - Total, used, and free space for each partition
  - Usage percentages

- **Process Monitoring**
  - Top 5 CPU-intensive processes
  - Top 5 memory-intensive processes

- **Additional System Information**
  - Operating system version
  - Kernel version
  - System uptime
  - Load averages
  - Currently logged-in users
  - Recent failed login attempts

## Requirements

- Linux-based operating system
- Bash shell
- Standard system utilities:
  - `top`
  - `ps`
  - `free`
  - `df`
  - `who`
  - `grep`
  - `awk`

## Installation

1. Clone or download the script:
```bash
curl -O https://your-repository/server-stats.sh
# or
wget https://your-repository/server-stats.sh
```

2. Make the script executable:
```bash
chmod +x server-stats.sh
```

## Usage

Simply run the script:
```bash
./server-stats.sh
```

The script will display all information in a formatted output to the terminal.

## Output Example

```
=== SERVER PERFORMANCE REPORT ===
Time: 2025-01-07 10:30:45
------------------------------------------------

=== OPERATING SYSTEM INFO ===
OS Version: Ubuntu 22.04.3 LTS
Kernel: 5.15.0-56-generic
Uptime: up 15 days, 7 hours, 23 minutes
Load average: 1.15, 0.95, 0.78

=== CPU STATISTICS ===
CPU Usage: 25.8%

=== MEMORY STATISTICS ===
Total Memory: 16.0G
Used: 8.2G (51%)
Free: 4.8G (30%)
Buffer/Cache: 3.0G

...
```

## Customization

You can modify the script to:
- Change the number of processes displayed (currently set to top 5)
- Add additional system metrics
- Modify the output format
- Add custom monitoring parameters

Edit the script file and adjust the relevant sections as needed.

## Troubleshooting

### Common Issues

1. **Permission Denied**
   ```bash
   bash: ./server-stats.sh: Permission denied
   ```
   Solution: Ensure the script has execution permissions
   ```bash
   chmod +x server-stats.sh
   ```

2. **Auth.log Not Found**
   - This is normal on some distributions that use different logging systems
   - The script will continue to function and display other metrics

### Known Limitations

- The script requires root/sudo access to read certain system files
- Some statistics might not be available on all Linux distributions
- Process statistics are point-in-time snapshots

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

@trxngxx

## Acknowledgments

- Inspired by various system monitoring tools
- Thanks to the Linux community for the robust command-line tools that make this possible