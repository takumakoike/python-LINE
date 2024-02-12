#coding:UTF-8
import os
from dotenv import load_dotenv
import requests

# LINE notifyからトークンの取得
# .envファイルの内容を読み込見込む
load_dotenv()
KEY = os.environ['LINE_TOKEN']

def main():
    url = "https://notify-api.line.me/api/notify"
    token = KEY
    headers = {"Authorization" : "Bearer "+ token}

    message = 'アラートがあります。\n賞味期限切れの商品があります。ご注意ください。'
    payload = {"message" : message}

    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    main()
