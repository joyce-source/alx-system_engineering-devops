#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    # Construct the URL to query the subreddit's information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, IndexError):
            # Invalid subreddit or error in API response
            return 0
    else:
        # Invalid subreddit or error in API response
        return 0

if __name__ == '__main__':
    subreddit = input("Enter the subreddit: ")
    num_subscribers = number_of_subscribers(subreddit)
    print(f"Number of subscribers in '{subreddit}': {num_subscribers}")
