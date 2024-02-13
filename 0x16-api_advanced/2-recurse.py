#!/usr/bin/pythoni2
import requests

def recurse(subreddit, hot_list=[], after=None):
    # Set a custom User-Agent to avoid Too Many Requests error
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'
    headers = {'User-Agent': 'Custom User Agent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']
            for post in posts:
                hot_list.append(post['data']['title'])

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
    else:
        # Invalid subreddit or error in API response
        return None
