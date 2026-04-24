#!/usr/bin/python3
import requests
import csv
"""asd sd"""



def fetch_and_print_posts():
    """asd sdf"""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Status code: {}".format(r.status_code))

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """sads e """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code == 200:
        """sdfd"""

        posts = r.json()
        data_to_save = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

    with open('posts.csv', mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(data_to_save)
