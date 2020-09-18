#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed
for a given subreddit."""

import requests


def top_ten(subreddit):
    """Function that queries Reddit API"""
    uri = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "My-User-Agent"}

    sub_info = requests.get(uri, headers=header, allow_redirects=False)
    if sub_info.status_code >= 300:
        print("None")
    else:
        for element in sub_info.json().get('data').get('children'):
            print(element.get("data").get("title"))
