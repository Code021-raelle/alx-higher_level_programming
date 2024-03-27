#!/bin/bash
# This script sends a GET request to a given URL with a specific header and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
