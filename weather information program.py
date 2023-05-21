# -*- coding: utf-8 -*-
"""
Created on Sun May 21 16:09:46 2023

@author: Cafer Karali
"""

import requests
import json
from datetime import datetime
#OpenWeatherMap API'ye istek göndererek hava durumu verilerini alma
def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"

    response = requests.get(url)
    data = json.loads(response.text)
#Hava durumu verilerini işleme
    if data["cod"] == "200":
        #yanıt kontrolu
        forecast_list = data["list"]

        for forecast in forecast_list:
            timestamp = forecast["dt"]
            date = datetime.fromtimestamp(timestamp)
            day = date.strftime("%Y-%m-%d")

            if date.hour == 12:  # saat 12 verilerini alıyoruz
                temperature = forecast["main"]["temp"]
                humidity = forecast["main"]["humidity"]
                description = forecast["weather"][0]["description"]

                print(f"Tarih: {day}")
                print(f"Hava Durumu: {description}")
                print(f"Sıcaklık: {temperature} °C")
                print(f"Nem Oranı: {humidity}%")
                print("*************************")

    else:
        print("Hava durumu bilgileri alınamadı.")

def main():
    api_key = 'YOUR_API_KEY' #bu kısma kendi API KEY'nizi yazmanız gerekiyor
    city = "Alanya"#başka bir bölgede sorgulayabilirsiniz

    get_weather(api_key, city)

if __name__ == "__main__":
    main()
