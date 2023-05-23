#!/bin/bash

# Prompt the user to enter the source directory
read -p "Enter the source directory where the Elasticsearch logs are located: " source_dir

# Prompt the user to enter the backup directory
read -p "Enter the backup directory where the backups will be stored: " backup_dir

# Check if the source directory exists
if [ ! -d "$source_dir" ]; then
    echo "Error: Source directory does not exist."
    exit 1
fi

# Check if the backup directory exists, and create it if necessary
if [ ! -d "$backup_dir" ]; then
    echo "Creating backup directory: $backup_dir"
    mkdir -p "$backup_dir"
fi

# Create a timestamp for the backup filename
timestamp=$(date +"%Y%m%d%H%M%S")

# Function to perform the backup
perform_backup() {
    local log_file="$1"
    
    # Check if the log file exists
    if [ -f "$log_file" ]; then
        # Create the backup filename with a timestamp
        backup_filename="${log_file}.${timestamp}.tar.gz"
        
        # Create the tar archive of the log file
        tar -czf "$backup_dir/$backup_filename" "$log_file"
        
        # Print a success message
        echo "Successfully backed up $log_file to $backup_dir/$backup_filename"
    else
        # Print an error message if the log file doesn't exist
        echo "Error: $log_file does not exist"
    fi
}

# Perform the backup for each Elasticsearch log file
perform_backup "$source_dir/elasticsearch.log"
perform_backup "$source_dir/elasticsearch-access.log"
perform_backup "$source_dir/elasticsearch_deprecation.log"
