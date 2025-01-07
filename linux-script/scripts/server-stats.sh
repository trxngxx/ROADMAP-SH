#!/bin/bash

# Function to print section headers
print_header() {
    echo -e "\n=== $1 ===\n"
}

# Function to print OS information
print_os_info() {
    print_header "OPERATING SYSTEM INFO"
    echo "OS Version: $(cat /etc/os-release | grep PRETTY_NAME | cut -d '"' -f 2)"
    echo "Kernel: $(uname -r)"
    echo "Uptime: $(uptime -p)"
    echo "Load average: $(uptime | awk -F'load average:' '{print $2}')"
}

# Function to print CPU usage
print_cpu_usage() {
    print_header "CPU STATISTICS"
    top -bn1 | grep "Cpu(s)" | awk '{print "CPU Usage: " $2 + $4 "%"}'
}

# Function to print memory usage
print_memory_usage() {
    print_header "MEMORY STATISTICS"
    free -h | awk '
    /^Mem:/ {
        print "Total Memory: " $2
        print "Used: " $3 " (" int($3/$2*100) "%)"
        print "Free: " $4 " (" int($4/$2*100) "%)"
        print "Buffer/Cache: " $6
    }'
}

# Function to print disk usage
print_disk_usage() {
    print_header "DISK USAGE"
    df -h | awk '
    /^\/dev/ {
        print "Partition: " $1
        print "Total Size: " $2
        print "Used: " $3 " (" $5 ")"
        print "Free: " $4
        print "--------------------"
    }'
}

# Function to print top CPU consuming processes
print_top_cpu_processes() {
    print_header "TOP 5 CPU-INTENSIVE PROCESSES"
    ps aux --sort=-%cpu | head -6 | awk '
    NR==1 {
        printf "%-10s %-10s %-10s %-40s\n", "PID", "USER", "%CPU", "COMMAND"
        print "------------------------------------------------"
    }
    NR>1 {
        printf "%-10s %-10s %-10s %-40s\n", $2, $1, $3, $11
    }'
}

# Function to print top memory consuming processes
print_top_memory_processes() {
    print_header "TOP 5 MEMORY-INTENSIVE PROCESSES"
    ps aux --sort=-%mem | head -6 | awk '
    NR==1 {
        printf "%-10s %-10s %-10s %-40s\n", "PID", "USER", "%MEM", "COMMAND"
        print "------------------------------------------------"
    }
    NR>1 {
        printf "%-10s %-10s %-10s %-40s\n", $2, $1, $4, $11
    }'
}

# Function to print logged in users
print_logged_users() {
    print_header "CURRENTLY LOGGED IN USERS"
    who | awk '{print $1 " - logged in from " $5 " at " $3 " " $4}'
}

# Function to print failed login attempts
print_failed_logins() {
    print_header "FAILED LOGIN ATTEMPTS"
    if [ -f /var/log/auth.log ]; then
        grep "Failed password" /var/log/auth.log | tail -5 | awk '{print $1 " " $2 " - " $(NF-5) " from " $(NF-3)}' || echo "Cannot read auth.log"
    else
        echo "Auth.log file not found"
    fi
}

# Main execution
clear
echo "=== SERVER PERFORMANCE REPORT ==="
echo "Time: $(date '+%Y-%m-%d %H:%M:%S')"
echo "------------------------------------------------"

# Call all functions
print_os_info
print_cpu_usage
print_memory_usage
print_disk_usage
print_top_cpu_processes
print_top_memory_processes
print_logged_users
print_failed_logins