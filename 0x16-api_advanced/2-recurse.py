#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    # Construct the URL to query the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            
            if not posts:
                return None

            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            # Check if there's a 'next page' token ('after') for pagination
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        except (KeyError, IndexError):
            # Invalid subreddit or error in API response
            return None
    else:
        # Invalid subreddit or error in API response
        return None

if __name__ == '__main__':
    subreddit = input("Enter the subreddit: ")
    result = recurse(subreddit)
    if result is not None:
        print(f"Number of hot articles: {len(result)}")
    else:
        print("None")
