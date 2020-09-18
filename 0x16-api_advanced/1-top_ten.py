#!/usr/bin/python3
"""titles of the first 10 hot posts listed"""
import json
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit
    API and prints the titles of the first 10 hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': 'somarae8'}
    query = requests.get(url, headers=header, allow_redirects=False)

    if query.status_code != 200:
        print(None)
    else:
        for title in query.json()['data']['children']:
            print(title['data']['title'])
