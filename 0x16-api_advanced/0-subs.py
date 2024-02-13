#!/usr/bin/python3
"""script defines a function to query and retrive subs for subreddit"""
import requests

def number_of_subscribers(subreddit):
  """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid or unavailable.
    """

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Construct the URL to query the subreddit's information
  url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Send a GET request to the Reddit API
  response = requests.get(url, headers=headers)

    # Check if the response is successful
  if response.status_code == 200:
        data = response.json()
  return data['data']['subscribers']
  else:
      return 0
