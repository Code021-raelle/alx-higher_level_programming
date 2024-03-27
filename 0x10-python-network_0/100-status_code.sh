#!/bin/bash
# This script sends a request to a given URL and displays only the status code of the response

# Check if a URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send a request to the URL and display only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
