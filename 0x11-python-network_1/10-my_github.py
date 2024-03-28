#!/usr/bin/python3
"""
This script takes Github credentials (username and personal access token) and
uses the Github API to display the user's id.
"""

import requests
import sys


if __name__ == "__main__":
    username = 'Code021-raelle'
    password = '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'

    response = requests.get('https://api.github.com/user',
            auth=(username, password))
    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print(None)
