#/usr/bin/python3

import time
import requests
from PIL import Image
from urllib.request import urlretrieve

client_id = 'a0ee951a-1a0b-4fa2-91fb-173f556002c'

directory = '/root/blog_flask/my_spirit_home/static/assets/img'
filename = directory + '/bg.jpg'
bg_blur = directory + '/bg_blur.jpg'
today = time.strftime("%Y-%m-%d")

headers = {
    'Host': 'api.momentumdash.com',
    'Accept': '*/*',
    'X-Momentum-ClientId': client_id,
    'X-Momentum-Version': '0.92.2',
    'X-Momentum-ClientDate': today,
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Content-Type': 'application/json',
    'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2d1aWQiOiJhZjAxOTFiMi1lOTM3LTRiM2ItYjM0OS01MDAzYWQ1OWVmNmEiLCJpc3MiOiJsb2dpbi1hcGktdjEiLCJleHAiOjE1MTcxMjk4NTAsIm5iZiI6MTQ4NTU5Mzg1MH0.pBfEBUQYZnF0vHCv8I_h8PWDr3bkfqAhjZ-toRc1x6U'
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
