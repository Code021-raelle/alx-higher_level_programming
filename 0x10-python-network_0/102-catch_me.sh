#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me and displays the response

# Send a request to the specified URL and output the response directly
curl -sL -X PUT -H -d "user_id=98" 0.0.0.0:5000/catch_me
