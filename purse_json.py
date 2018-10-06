# coding: UTF-8

from pathlib import Path
import json
import csv

def make_address(location_name, address_json):
    # print(address_json)
    cd = address_json['country_code']
    address = location_name
    if address_json['street_address'] is not None and address_json['street_address'] is not "":
        address += ', ' + address_json['street_address']

    if address_json['city_name'] is not None and address_json['city_name'] is not "":
        address += ', ' + address_json['city_name']

    if address_json['region_name'] is not None and address_json['region_name'] is not "":
        address += ', ' + address_json['region_name']
    address += ', ' + cd
    return address

def func2(photo_dic):
    dic = {}
    # print(photo_dic['location'])
    dic['url'] = 'https://www.instagram.com/p/' + photo_dic['shortcode'] + '/'
    dic['image_url'] = photo_dic['display_url']
    dic['username'] = photo_dic['username']
    dic['user_id'] = photo_dic["owner"]["id"]
    dic['timestamp'] = photo_dic['taken_at_timestamp']
    # print(photo_dic['location']['address_json'])
    try:
        json.loads(photo_dic['location']['address_json'])
    except Error as e:
        print(photo_dic)
        print('JSONDecodeError: ', e)

    address_json = json.loads(photo_dic['location']['address_json'])
    dic['country_code'] = address_json['country_code']
    # print(photo_dic['location']['id'])
    dic['address'] = make_address(photo_dic['location']['name'], address_json)
    # print(dic['address'])
    return dic


def func(file_path):
    print(file_path.name)
    f = open(file_path, 'r', encoding='utf-8')
    json_dict = json.load(f)
    list = []
    # この中からaddress_jsonのあるものだけ次のメソッドに流す。
    for photo_dic in json_dict:
        if photo_dic['location'] is not None and photo_dic['location']['address_json'] is not None :
            list.append(func2(photo_dic))

    return list

def write_tsv_header(file_name):
    with open(file_name, "w", newline="") as f:
        fieldnames = ["user_id", "username", "url", "image_url", "timestamp", "country_code", "address"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", quotechar='"')
        writer.writeheader()


def write_tsv_body(file_name, a_user_list):
    with open(file_name, "a", newline="") as f:
        fieldnames = ["user_id", "username", "url", "image_url", "timestamp", "country_code", "address"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", quotechar='"')
        # writerowで1行分を出力します.
        for v in a_user_list:
            writer.writerow({"user_id": v["user_id"], "username": v["username"], "url": v["url"], "image_url": v["image_url"], "timestamp": v["timestamp"], "country_code": v["country_code"], "address": v["address"] })


# Pathオブジェクトを生成
p = Path("./images_jsons/")
files = list(p.glob("*.json"))

write_tsv_header("b.tsv")

# user_list = []
# list = [func(file) for file in files]
# func(files[0], a_user_list)
for file in files:
    a_user_list = func(file)
    write_tsv_body("b.tsv", a_user_list)
    #     ファイル書き込み

# def func(file):
#     print(file.name)
# print(a_user_list)


