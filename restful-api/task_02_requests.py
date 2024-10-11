import requests
import csv


"""Consuming and processing data from an API using Python"""


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

    for post in posts:
        print(post['title'])

    else:
        ("failed to fetch data.")


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:

        posts = response.json()

    with open("posts.csv", mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for post in posts:
            writer.writerow({'id': post['id'], 'title': post[
                    'title'], 'body': post['body']})


print("Data saved to posts.csv successfully!")
