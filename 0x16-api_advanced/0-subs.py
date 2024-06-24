#!/usr/bin/python3
'''module'''
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Unfortunately I had to use a custom one'}
    req = requests.get(url, headers=headers).json()
    nums = req.get('data', {}).get('subscribers', 0)
    return nums
