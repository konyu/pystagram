# coding: UTF-8

import urllib.request
import json

# [Xiaobei Station - Instagram • 写真と動画](https://www.instagram.com/explore/locations/346112693/xiaobei-station/)　
# location idでその場所のIDを取得する
# instagram-scraper --location 346112693  -u <自分のID> -p <自分のパスワード> --maximum 1000 --media-metadata --include-location
f = open('346112693.json', 'r')
json_dict = json.load(f)
print('json_dict:{}'.format(type(json_dict)))
# // "shortcode" 配列のshortcordeを取得して、配列に格納する

shortcodes = [v["shortcode"] for v in json_dict]
# print(shortcodes)

# owner iDでDictionaryを作る
owner_dict = {}
for v in json_dict:
    owner_dict[v["owner"]["id"]] = v["shortcode"]

# 368個データが有る
# print(owner_dict)

# 配列から　https://www.instagram.com/p/ショートコード/?__a=1 にアクセスして、JSONを取得する
url = "https://www.instagram.com/p/{SHORTCODE}/?__a=1"

username_list = []
for v in list(owner_dict.values()):
    try:
        combined_url = url.replace('{SHORTCODE}', v)
        # print(combined_url)

        response = urllib.request.urlopen(combined_url)
        content = json.loads(response.read().decode('utf8'))
        username = content["graphql"]["shortcode_media"]["owner"]["username"]
        username_list.append(username)
    except urllib.error.HTTPError as e:
        print('HTTPError: ', e)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

print(username_list)

# ユーザ名のリストをファイルに書き込む
file_name = "./username_list.txt"

try:
    file = open(file_name, 'a')
    for v in username_list:
        file.write(v + "\n")
except Exception as e:
    print(e)
finally:
    file.close()
