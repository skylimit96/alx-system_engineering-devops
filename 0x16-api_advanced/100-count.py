#!/usr/bin/python3
"""
Function count
"""
import re
import requests


def add_title(dictionary, hot_posts):
    """ Adds item into a list title """
    if not hot_posts:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        word = re.sub(r'[^\w\s]', '', word).lower()
        if word in dictionary:
            dictionary[word] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ Adds item into a recurse """
    u_agent = 'My User Agent 1.0'
    headers = {'User-Agent': u_agent}
    params = {'after': after}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return

    data = res.json()
    hot_posts = data['data']['children']
    add_title(dictionary, hot_posts)

    after = data['data']['after']
    if after:
        recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ count_words """
    dictionary = {}
    for word in word_list:
        dictionary[word.lower()] = 0

    recurse(subreddit, dictionary)

    sorted_words = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        if count > 0:
            print(f"{word}: {count}")
