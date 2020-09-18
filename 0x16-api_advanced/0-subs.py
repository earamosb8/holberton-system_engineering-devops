#!/usr/bin/python3

"""function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'craw90'}
    info = requests.get(url, headers=header, allow_redirects=False)
    if info.status_code == 200:
        return info.json()['data']['subscribers']
    return 0


if __name__ == "__main__":
    pass
