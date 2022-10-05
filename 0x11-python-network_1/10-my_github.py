#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'

    res = requests.post(
        url, auth=requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    res_json = res.json()
    print(res_json.get('id'))
