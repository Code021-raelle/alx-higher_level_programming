#!/bin/bash
# This script sends a GET request to a given URL and displays the body of the response if the status code is 200

# Check if a URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send a GET request to the URL and check the status code
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# If the status code is 200, display the body of the response
if [ "$status_code" -eq 200 ]; then
	curl -s "$1"
else
	echo "Request failed with status code: $status_code"
fi
