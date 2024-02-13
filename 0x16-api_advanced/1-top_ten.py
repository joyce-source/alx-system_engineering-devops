#!/usr/bin/python3
import requests

def top_ten(subreddit):
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
