#!/usr/bin/python3
"""script to retrieve titles of the top 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """
    Retrieve the titles of the top 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: If the subreddit is not found or an error occurs.
    """
    # Set a custom User-Agent to avoid Too Many Requests error
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User Agent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
