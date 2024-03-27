#!/bin/bash
# This script sends an OPTIONS request to a given URL and displays the allowed HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
