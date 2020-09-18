#!/usr/bin/python3
"""Recurse"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Function that queries Reddit API"""
    uri = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "My-User-Agent"}
    param = {"count": count, "after": after}

    sub_info = requests.get(uri, params=param, headers=header,
                            allow_redirects=False)
    if sub_info.status_code >= 400:
        return None

    hot = hot_list + [child.get("data").get("title")
                      for child in sub_info.json()
                      .get("data")
                      .get("children")]

    kind = sub_info.json()
    if not kind.get("data").get("after"):
        return hot

    return recurse(subreddit, hot,
                   kind.get("data").get("count"),
                   kind.get("data").get("after"))
