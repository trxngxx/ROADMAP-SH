#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 <log-directory>"
    echo "Example: $0 /var/log"
    exit 1
}

# Function to validate directory
validate_directory() {
    local dir=$1
    
    # Check if directory argument is provided
    if [ -z "$dir" ]; then
        echo "Error: Log directory not specified"
        usage
    fi
    
    # Check if directory exists
    if [ ! -d "$dir" ]; then
        echo "Error: Directory '$dir' does not exist"
        exit 1
    fi
    
    # Check if directory is readable
    if [ ! -r "$dir" ]; then
        echo "Error: Cannot read directory '$dir'. Please check permissions"
        exit 1
    fi
}

# Function to create archive directory if it doesn't exist
create_archive_dir() {
    local archive_dir="$1"
    if [ ! -d "$archive_dir" ]; then
        mkdir -p "$archive_dir"
        if [ $? -ne 0 ]; then
            echo "Error: Failed to create archive directory"
            exit 1
        fi
    fi
}

# Main function to archive logs
archive_logs() {
    local log_dir=$1
    local current_date=$(date +%Y%m%d_%H%M%S)
    local archive_name="logs_archive_${current_date}.tar.gz"
    local archive_dir="./archived_logs"
    
    # Validate input directory
    validate_directory "$log_dir"
    
    # Create archive directory
    create_archive_dir "$archive_dir"
    
    # Create archive
    echo "Creating archive from $log_dir..."
    tar -czf "$archive_dir/$archive_name" -C "$log_dir" .
    
    if [ $? -eq 0 ]; then
        echo "Successfully created archive: $archive_dir/$archive_name"
        
        # Log the archive creation
        echo "$(date): Created archive $archive_name from $log_dir" >> "$archive_dir/archive_history.log"
        
        # Show archive details
        echo -e "\nArchive details:"
        echo "Location: $archive_dir/$archive_name"
        echo "Size: $(du -h "$archive_dir/$archive_name" | cut -f1)"
        echo "Files included: $(tar -tf "$archive_dir/$archive_name" | wc -l)"
    else
        echo "Error: Failed to create archive"
        exit 1
    fi
}

# Check for --help flag
if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    usage
fi

# Execute main function with provided directory
archive_logs "$1"