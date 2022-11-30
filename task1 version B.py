# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:47:36 2022

@author: HP
"""

#############################################################

# Question 1 Return a list of Top Posts ordered by their
# number of comments

import json
import turtle
import urllib.request
import time
import webbrowser
import requests


# Question 1(a) Comments endpoint
url = "https://jsonplaceholder.typicode.com/comments"
response1 = urllib.request.urlopen(url) 
result1 = json.loads(response1.read())
result1

# Question 1(b)
# View single post endpoint
url = "https://jsonplaceholder.typicode.com/posts/2"
response2 = urllib.request.urlopen(url) 
result2 = json.loads(response2.read())
result2

url = "https://jsonplaceholder.typicode.com/posts/5"
response3 = urllib.request.urlopen(url) 
result3 = json.loads(response3.read())
result3


# Question 1(c)
# View all posts endpoint
url = "https://jsonplaceholder.typicode.com/posts"
response4 = urllib.request.urlopen(url) 
result4 = json.loads(response4.read())
result4

###############################################################



###############################################################

# Question 2 Search API Create an endpoint that allows a
# user to filter the comments based on all the available fields.
# Your solution needs to be scalable.
# comments endpoint

# Query by 1 resource
query_params = {"postId":"99"}
url = "https://jsonplaceholder.typicode.com/comments"
response5 = requests.get(url, params=query_params)
response5.json()

query_params1 = {"id":"494"}
url = "https://jsonplaceholder.typicode.com/comments"
response6 = requests.get(url, params=query_params1)
response6.json()

query_params2 = {"name":"ut praesentium sit eos rerum tempora"}
url = "https://jsonplaceholder.typicode.com/comments"
response7 = requests.get(url, params=query_params2)
response7.json()

query_params3 = {"email":"Maxwell@adeline.me"}
url = "https://jsonplaceholder.typicode.com/comments"
response8 = requests.get(url, params=query_params3)
response8.json()

################################################################



################################################################

# Scaling up / Query by multiple resource
query_params4 = {"postId":"99", "id":"493"}
url = "https://jsonplaceholder.typicode.com/comments"
response9 = requests.get(url, params=query_params4)
response9.json()

query_params5 = {"postId":"21", "id":"102", "email":"Lottie.Zieme@ruben.us"}
url = "https://jsonplaceholder.typicode.com/comments"
response10 = requests.get(url, params=query_params5)
response10.json()

################################################################




    





 
