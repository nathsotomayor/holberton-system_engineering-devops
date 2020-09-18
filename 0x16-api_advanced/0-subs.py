#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries Reddit API"""
    uri = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "My-User-Agent"}

    sub_info = requests.get(uri, headers=header, allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get('data', {}).get('subscribers', 0)
