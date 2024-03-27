#!/bin/bash
# This script sends a request to a given URL and displays the size of the response body in bytes

# Check if a URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send a request to the URL and get the size of the response bosy in bytes
response_size=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# Display the size
echo $response_size
