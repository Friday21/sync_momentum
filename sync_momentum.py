#/usr/bin/python3

import time
import requests
from PIL import Image
from urllib.request import urlretrieve

client_id = '这里是你自己chrome 访问插件Momentum的ID， 打开个新窗口看下访问数据就知道了'

directory = '/root/blog_flask/my_spirit_home/static/assets/img'
filename = directory + '/bg.jpg'
bg_blur = directory + '/bg_blur.jpg'
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
    new_img_blur = img.resize((153, 102), Image.ANTIALIAS)
    new_img_blur.save(bg_blur, quility=100)
