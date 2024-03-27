#!/bin/bash
# This script sends a GET request to a given URL and displays the body of the response if the status code is 200
curl -sL -w "%{http_code}" -o /dev/null "$1" | {
	read -r status_code
	if [[ $status_code -eq 200 ]]; then
		curl -sL "$1"
	fi
}
