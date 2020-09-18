#!/usr/bin/python3
"""
titles of the first 10 hot posts listed
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of
    all hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'somarae8'}
    info = requests.get(url, headers=header, allow_redirects=False,
                        params={'after': after})
    if info.status_code != 200:
        return None
    else:
        after = info.json()['data']['after']
        if after is None:
            return hot_list
        for post in info.json()['data']['children']:
            hot_list.append(post['data']['title'])
        return recurse(subreddit, hot_list, after)
