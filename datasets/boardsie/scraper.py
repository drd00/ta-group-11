import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import hashlib

forum_root = "https://www.boards.ie/categories/politics-politics/p"

def get_thread_posts(thread_url):
    try:
        response = requests.get(thread_url, timeout=5)

        bs = BeautifulSoup(response.text, "html.parser")
        comments = bs.find_all('div', class_='Comment')
        posts_auth = {}

        for comment in comments:
            user = comment.find("div", class_="userinfo-username")
            user = user.find("a")['href'].replace('https://www.boards.ie/profile/', '')
            message = comment.find_all("div", class_="Message userContent")
            message_text = ' '.join(paragraph.get_text(strip=True) for paragraph in message)

            if user in posts_auth:
                posts_auth[user].append(message_text)
            else: 
                posts_auth[user] = [message_text]
        
        return posts_auth
    except Exception as e:
        print(f'Some error {e}')
        return {}

n_pages = 20
user_post_tuples = []
for i in range(n_pages):
    print(f"--------------------------\n---------------------------\nPAGE {i} --------------------------\n---------------------------\n")
    forum_page = forum_root + str(i+1)
    response = requests.get(forum_page)
    soup = BeautifulSoup(response.text, "html.parser")
    threads = soup.find_all("a", class_="threadbit-threadlink")
    all_posts = []
    for thread in threads:
        thread_posts = get_thread_posts(thread.get('href'))
        if thread_posts:
            thread_id = hashlib.sha256(thread.get('href').encode()).hexdigest()
            user_post_tuples.extend([(thread_id, hashlib.sha256(user.encode()).hexdigest(), post) for user, posts in thread_posts.items() for post in posts])
            print(user_post_tuples)
            time.sleep(1)   # let's not make them too mad
    
df = pd.DataFrame(user_post_tuples, columns=['thread_id', 'user', 'post'])
df.to_csv('boards_ie_politics.csv', index=False, encoding='utf-8-sig') 

