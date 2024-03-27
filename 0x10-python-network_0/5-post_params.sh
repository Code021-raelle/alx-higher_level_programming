#!/bin/bash
# This script sends a POST request to a given URL with specific parameters and displays the body of the response

# Check if a URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send a POST request to the URL with the specified parameters and display the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
