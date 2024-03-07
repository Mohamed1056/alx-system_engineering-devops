#!/usr/bin/python3
"""Script for returning the hotest 10 posts."""

import requests


def top_ten(subreddit):
    '''function to return the hotest 10 possts.'''
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
            "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) forc in results.get("childern")]
