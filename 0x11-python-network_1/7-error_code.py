#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code"""

import sys
import requests

if __name__ == '__main__':
    bodyRes = requests.get(sys.argv[1])
    if bodyRes.status_code >= 400:
        print('Error code: {}'.format(bodyRes.status_code))
    else:
        print(bodyRes.text)
