#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Thu Sep 21 03:39 2023
@author: Anita Ododo
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None.
    """
    if not subreddit:
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': 'Your User Agent Here'
    }
    params = {'after': after}
    
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch data for subreddit: {subreddit}")
        return None

    data = response.json()
    children = data.get('data', {}).get('children', [])

    for title in children:
        hot_list.append(title.get('data', {}).get('title'))

    after = data.get('data', {}).get('after')

    if after:
        # Recursive call to fetch the next page
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list

# Example usage:
# hot_articles = recurse('programming')
# print(hot_articles)


