import requests
import time
from t import TOKEN as token
from bs4 import BeautifulSoup
from flask import Flask, request
import translators as ts

app = Flask(__name__)

CHANNEL_ID = "borna_gym"

URL = "https://www.rt.com/news/"

def get_text_from_website():
    try:
        #li.listCard-rows__item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)
        pic = 'div.widgetGrid-widget-item:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > picture:nth-child(1) > img:nth-child(3)'
        cs1 = 'li.listCard-rows__item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)'
        cs2 = 'li.listCard-rows__item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)'
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            element = soup.select_one(cs1)
            element2 = soup.select_one(cs2)
            p = soup.select_one(pic)

            if element and element2:
                t1 = element.text.strip()
                t2 = element2.text.strip()
                p1 = p.get('src')
                print(p1)

                link1 = element['href']

                linkk1 = 'https://www.rt.com' + link1

                textkol = f"{t1}\n{t2}\n\n{linkk1}"
                return textkol 
    except Exception as e:
        return e

def send_message_to(message):
    url = url = f"https://eitaayar.ir/api/{token}/sendMessage"
    
    payload = {"chat_id": CHANNEL_ID, "text": message}
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print(message)
        print(response.json())
        print("پیام با موفقیت ارسال شد")
    else:
        print("خطا در ارسال پیام:", response.json())
        

@app.route("/", methods=["GET" , "POST"])
def home():
    return " ربات در حال اجرا است"

@app.route("/run_bot")
def run_bot_route():
    run_bot()
    return " ربات در حال کار!"

def run_bot():
    text = get_text_from_website()
    if text :
        send_message_to(text)
            


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)




