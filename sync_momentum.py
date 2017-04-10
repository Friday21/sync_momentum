#/usr/bin/python3

import os
import time
import requests
from PIL import Image
from urllib.request import urlretrieve

client_id = 'a0ee951a-1a0b-4fa2-91fb-173f556002c2'

directory = '/root/blog_flask/my_spirit_home/static/assets/img'
filename = directory + 'bg.jpg'
today = time.strftime("%Y-%m-%d")

headers = {
    'Host': 'api.momentumdash.com',
    'Accept': '*/*',
    'X-Momentum-ClientId': client_id,
    'X-Momentum-Version': '0.92.2',
    'Content-Type': 'application/json'
}

r = requests.get('https://api.momentumdash.com/feed/bulk?syncTypes=backgrounds&localDate=' + today, headers=headers)
print(r.json())
image_list = r.json()['backgrounds']
image_url = ''
for image in image_list:
    if image['forDate'] == today:
        image_url = image['filename']
if image_url:
    urlretrieve(image_url, filename)
    img = Image.open(filename)
    new_img = img.resize((1536, 1023), Image.ANTIALIAS)
    new_img.save(filename, quility=100)