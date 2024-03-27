#!/bin/bash
# This script sends an OPTIONS request to a given URL and displays the allowed HTTP methods

# Check if a URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send an OPTIONS request to the URL and extract the Allow header
allowed_methods=$(curl -s -X OPTIONS -I "$1" | grep -i "Allow:" | awk '{print $2}')

# Display the allowed methods
echo $allowed_methods
