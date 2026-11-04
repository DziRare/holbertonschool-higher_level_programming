#!/usr/bin/python3
"""This module fetches posts from JSONPlaceholder."""

import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """This function festches all posts, print the status code."""
    response = requests.get(URL)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """This function is for fetching all posts and save them to posts.csv."""
    response = requests.get(URL)
    if response.status_code == 200:
        posts = response.json()
        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
