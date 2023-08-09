#!/usr/bin/python3
import requests

def top_ten(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    # Construct the URL to query the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            if not posts:
                print("No posts found.")
            else:
                for post in posts:
                    title = post['data']['title']
                    print(title)
        except (KeyError, IndexError):
            # Invalid subreddit or error in API response
            print("None")
    else:
        # Invalid subreddit or error in API response
        print("None")

if __name__ == '__main__':
    subreddit = input("Enter the subreddit: ")
    top_ten(subreddit)
