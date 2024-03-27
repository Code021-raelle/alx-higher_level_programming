#!/bin/bash
# This script sends a JSON POST request to a given URL with the contents of a file in the body of the request

# Check if a URL and a filename are provided
if [ -z "$1" ] || [ -z "$2" ]; then
	echo "Usage: $0 <URL> <filename>"
	exit 1
fi

# Send a POST request to the URL with the contents of the file in the body of the request
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
