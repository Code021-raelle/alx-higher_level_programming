#!/bin/bash
# This script sends a request to a given URL and displays the size of the response body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
