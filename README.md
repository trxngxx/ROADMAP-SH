# Nginx Log Analyser

Project URL: https://roadmap.sh/projects/nginx-log-analyser

A command-line tool to analyze Nginx access logs and generate useful statistics. This tool helps system administrators and developers understand their web traffic patterns by analyzing various aspects of Nginx access logs.

## Features

The tool analyzes Nginx access logs and provides the following information:
- Top 5 IP addresses with the most requests
- Top 5 most requested paths
- Top 5 response status codes with descriptions
- Top 5 user agents
- General statistics including total requests, unique IPs, and time range

## Requirements

- Unix-like operating system (Linux, macOS)
- Bash shell
- Basic text processing utilities (awk, sort, uniq)
- Nginx access log file

## Installation

1. Download the script:
```bash
curl -O https://github.com/trxngxx/ROADMAP-SH.git
# or
wget https://github.com/trxngxx/ROADMAP-SH.git
```

2. Make it executable:
```bash
chmod +x nginx-log-analyser
```

3. Optionally, move to system path:
```bash
sudo mv nginx-log-analyser /usr/local/bin/
```

## Usage

Basic usage:
```bash
./nginx-log-analyser <nginx-access-log-file>
```

Example:
```bash
./nginx-log-analyser /var/log/nginx/access.log
```

## Output Example

```
=== Nginx Log Analysis Report ===
Analyzing file: /var/log/nginx/access.log
Generated on: 2024-01-07 12:34:56
----------------------------------------

=== General Statistics ===
Total Requests: 15729
Unique IP Addresses: 342
Time Range: 07/Jan/2024:00:00:01 to 07/Jan/2024:23:59:59

=== Top 5 IP Addresses with Most Requests ===
192.168.1.100   1234 requests
10.0.0.50       987 requests
172.16.0.25     654 requests
192.168.1.200   432 requests
10.0.0.100      321 requests

=== Top 5 Most Requested Paths ===
/api/users          5432 requests
/static/main.css    3210 requests
/images/logo.png    2345 requests
/api/products       1234 requests
/about.html         987 requests

=== Top 5 Response Status Codes ===
200   (OK)                    12345 requests
404   (Not Found)             234 requests
500   (Internal Server Error) 123 requests
301   (Moved Permanently)     98 requests
403   (Forbidden)             45 requests

=== Top 5 User Agents ===
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36     3456 requests
Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)           2345 requests
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)                  1234 requests
Googlebot/2.1 (+http://www.google.com/bot.html)                  987 requests
curl/7.64.1                                                      654 requests
```

## Log File Format

The tool expects Nginx access logs in the default format:
```
$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"
```

Example log entry:
```
192.168.1.100 - - [07/Jan/2024:12:34:56 +0000] "GET /api/users HTTP/1.1" 200 1234 "http://example.com" "Mozilla/5.0"
```

## Customization

You can modify the script to:
- Change the number of items displayed in each category
- Add additional statistics
- Modify the output format
- Add filtering options
- Include more HTTP status code descriptions

## Error Handling

The script handles various error conditions:
- Missing log file argument
- Non-existent log file
- Permission issues
- Invalid log format

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Your Name]
[Your Contact Information]

## Acknowledgments

- Inspired by common web server log analysis needs
- Thanks to the Nginx and Unix/Linux communities