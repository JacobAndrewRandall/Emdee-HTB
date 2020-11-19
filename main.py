from hashlib import md5
from bs4 import BeautifulSoup as BS
import requests
url = ""


def encrypt_to_md5(string):
    test = md5(string.encode())
    return test.hexdigest()


s = requests.Session()
site = s.get(url)
if site.status_code == 200:
    soup = BS(site.text, features="html.parser")
    phrase = soup.find('h3').get_text()
    encrypted_phrase = encrypt_to_md5(phrase)
    post_request = s.post(url, data={'hash': encrypted_phrase})
    print(post_request.text)
else:
    print(f"Error getting to {url} Status code:{site.status_code}")
