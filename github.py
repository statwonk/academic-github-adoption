# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:21:47 2013

@author: chris
"""

import requests
import json
import csv
r = requests.get('https://api.github.com/search/repositories?q=language:latex')

if(r.ok):
    repoItem = json.loads(r.content)

print repoItem['total_count']

df = {}
for repo in repoItem['items']:
    df[repo['name']] = repo['created_at']
    
writer = csv.writer(open('data.csv', 'wb'))
for key, value in df.items():
    writer.writerow([key, value])
