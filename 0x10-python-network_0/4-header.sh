#!/bin/bash
# This script sends a GET request to a given URL with a specific header and displays the body of the response

# Check if a URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send a GET request to the URL with the specified header and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
