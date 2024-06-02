import requests
import csv

def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])
    else:
        print("Failed to retrieve posts")

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        csv_file = 'posts.csv'

        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)
        
        print(f"Data has been written to {csv_file}")
    else:
        print("Failed to retrieve posts")
