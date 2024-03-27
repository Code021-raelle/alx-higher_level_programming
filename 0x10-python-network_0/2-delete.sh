#!/bin/bash
# This script sends a DELETE request to a given URL and displays the body of the response

# Check if a URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send a DELETE request to the URL and display the body of the response
curl -s -X DELETE "$1"
