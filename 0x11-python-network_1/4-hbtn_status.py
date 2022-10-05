#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == '__main__':
    bodyRes = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(bodyRes.text)))
    print('\t- content: {}'.format(bodyRes.text))
