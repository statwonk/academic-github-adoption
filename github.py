# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:21:47 2013

@author: chris
"""

import requests
import json
import csv
import time

times = ["2010", "2011", "2012"]
for i in range(0, 12):
  times.append(str(str(2013) + "-" + str(i + 1)))

df = {}
for j in times:
    for i in range(1, 10):
        # print "Sleeping 10 seconds ... "    
        time.sleep(60/4)
        r = requests.get('https://api.github.com/search/repositories?q=language:latex&' + \
                         'page=' + str(i) + '&per_page=100' + \
                         '&created=' + str(j))
        if(r.ok):
            repoItem = json.loads(r.content)
            print "page " + str(i) + ", year " + str(j)
            for repo in repoItem['items']:
                df[repo['name']] = repo['created_at']
        else: print "oh nos! Page " + str(i) + " has a problem"

with open('data.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter= ',')
    for i in df.keys():
        writer.writerow((i, df[i]))