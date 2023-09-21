#!/usr/bin/python3
# -*- coding: utf-8 -*-

from requests import get

def recurse(subreddit, hot_list=[], after=None):
    """Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) '
        'Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    params = {'after': after} if after else {}
    
    response = get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data for subreddit '{subreddit}'")
        return None
    
    reddits = response.json()
    children = reddits.get('data', {}).get('children', [])

    if not children:
        return hot_list

    for title in children:
        hot_list.append(title.get('data', {}).get('title'))

    after = reddits.get('data', {}).get('after')

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list

# Example usage:
# hot_titles = recurse('python')
# print(hot_titles)
