#!/bin/bash
# This script sends a JSON POST request to a given URL with the contents of a file in the body of the request
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
