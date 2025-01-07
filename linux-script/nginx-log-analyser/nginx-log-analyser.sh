#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 <nginx-access-log-file>"
    echo "Example: $0 /var/log/nginx/access.log"
    exit 1
}

# Function to validate file
validate_file() {
    local file=$1
    
    # Check if file argument is provided
    if [ -z "$file" ]; then
        echo "Error: Log file not specified"
        usage
    fi
    
    # Check if file exists
    if [ ! -f "$file" ]; then
        echo "Error: File '$file' does not exist"
        exit 1
    fi
    
    # Check if file is readable
    if [ ! -r "$file" ]; then
        echo "Error: Cannot read file '$file'. Please check permissions"
        exit 1
    }
}

# Function to print section header
print_header() {
    echo -e "\n=== $1 ===\n"
}

# Function to get top IP addresses
get_top_ips() {
    local log_file=$1
    print_header "Top 5 IP Addresses with Most Requests"
    awk '{print $1}' "$log_file" | sort | uniq -c | sort -rn | head -n 5 | \
    awk '{printf "%-15s %s requests\n", $2, $1}'
}

# Function to get top requested paths
get_top_paths() {
    local log_file=$1
    print_header "Top 5 Most Requested Paths"
    awk '{print $7}' "$log_file" | sort | uniq -c | sort -rn | head -n 5 | \
    awk '{printf "%-50s %s requests\n", $2, $1}'
}

# Function to get top response status codes
get_top_status_codes() {
    local log_file=$1
    print_header "Top 5 Response Status Codes"
    awk '{print $9}' "$log_file" | sort | uniq -c | sort -rn | head -n 5 | \
    while read count status; do
        case $status in
            200) desc="OK";;
            301) desc="Moved Permanently";;
            302) desc="Found";;
            304) desc="Not Modified";;
            400) desc="Bad Request";;
            401) desc="Unauthorized";;
            403) desc="Forbidden";;
            404) desc="Not Found";;
            500) desc="Internal Server Error";;
            502) desc="Bad Gateway";;
            503) desc="Service Unavailable";;
            504) desc="Gateway Timeout";;
            *) desc="Unknown";;
        esac
        printf "%-5s %-20s %s requests\n" "$status" "($desc)" "$count"
    done
}

# Function to get top user agents
get_top_user_agents() {
    local log_file=$1
    print_header "Top 5 User Agents"
    awk -F'"' '{print $6}' "$log_file" | sort | uniq -c | sort -rn | head -n 5 | \
    awk '{$1=""; printf "%-80s %s requests\n", substr($0,2), $1}'
}

# Function to show general statistics
show_general_stats() {
    local log_file=$1
    print_header "General Statistics"
    
    # Total requests
    local total_requests=$(wc -l < "$log_file")
    echo "Total Requests: $total_requests"
    
    # Unique IPs
    local unique_ips=$(awk '{print $1}' "$log_file" | sort -u | wc -l)
    echo "Unique IP Addresses: $unique_ips"
    
    # Time range
    local start_date=$(head -n 1 "$log_file" | awk -F'[' '{print $2}' | awk -F']' '{print $1}')
    local end_date=$(tail -n 1 "$log_file" | awk -F'[' '{print $2}' | awk -F']' '{print $1}')
    echo "Time Range: $start_date to $end_date"
}

# Main function
main() {
    local log_file=$1
    
    # Validate input file
    validate_file "$log_file"
    
    # Display banner
    echo "=== Nginx Log Analysis Report ==="
    echo "Analyzing file: $log_file"
    echo "Generated on: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "----------------------------------------"
    
    # Show statistics
    show_general_stats "$log_file"
    get_top_ips "$log_file"
    get_top_paths "$log_file"
    get_top_status_codes "$log_file"
    get_top_user_agents "$log_file"
}

# Check for help flag
if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    usage
fi

# Execute main function
main "$1"