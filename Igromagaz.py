import json

import requests
from bs4 import BeautifulSoup

from Getter import Getter


class Igromagaz(Getter):
    

    def get_data(self):
        #req=requests.get(url=self.url,headers=self.headers)
        #with open(f"data/index_page.html","w",encoding="UTF-8") as file:
            #file.write(req.text)

        #with open (f"data/index_page.html",encoding="UTF-8") as file:
            #src=file.read() 

        #soup=BeautifulSoup(src,"lxml")
        #page_count=soup.find("a",class_="pagination__item pagination__item_last pagination-js")
        games=[]
        for i in range(1,3): #int(page_count)+1
            url_1=f"https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&PAGEN_1={i}"
            req=requests.get(url=url_1,headers=self.header)

            with open(f"data/index_{i}.html","w",encoding="UTF-8") as file:
                file.write(req.text)

            with open (f"data/index_{i}.html",encoding="UTF-8") as file:
                src=file.read() 
                
            soup=BeautifulSoup(src,"lxml")
            games_cards=soup.find_all("div",class_="product-tile__in")
            for cards in games_cards:
                name=cards.find("a",class_="product-tile__name")
                ref=cards.find("a",class_="product-tile__image").get("href")
                try:
                    old_price=cards.find("div",class_="product-tile__price-old")
                    new_price=cards.find("div",class_="product-tile__price")
                    avaliability=cards.find("div",class_="product-tile__stock")
                    games.append({
                        "Название":name.text.replace(" (ключ для ПК)",""),
                        "Cтарая цена":(old_price.text.strip().replace(" руб."," руб")),
                        "Новая цена":new_price.text+" руб",
                        "Наличие":avaliability.text.lower(),
                        "Cсылка":"https://www.igromagaz.ru"+ref
                        })
                except Exception as e:
                    print(e)
                    continue


        with open("igromagaz_discount.json","w",encoding="UTF-8") as file:
            json.dump(games,file,indent=4,ensure_ascii=False)

