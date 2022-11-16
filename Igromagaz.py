import json

import requests
from bs4 import BeautifulSoup


class Igromagaz():
  

    def get__data(self,genre):

        header={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }


        if genre=="strategy":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B12987%5D=12987"
        elif genre=="horror":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B23822%5D=23822"
        elif genre=="arcade":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B12993%5D=12993"
        elif genre=="children":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B23818%5D=23818"
        elif genre=="mindgames":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B23820%5D=23820"
        elif genre=="shooter":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B34392%5D=34392"
        elif genre=="indie":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B34394%5D=34394"
        elif genre=="casual":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B34395%5D=34395"
        elif genre=="race":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B13661%5D=13661"
        elif genre=="mmo":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B12984%5D=12984"
        elif genre=="action":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B12985%5D=12985"
        elif genre=="simulator":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B12988%5D=12988"
        elif genre=="adventure":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B12989%5D=12989"
        elif genre=="rpg":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B12990%5D=12990"
        elif genre=="fighting":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B12991%5D=12991"
        elif genre=="sport":
            url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&genres%5B12992%5D=12992"

        try:
            req=requests.get(url=url,headers=header)
            with open(f"data/index_page.html","w",encoding="UTF-8") as file:
                file.write(req.text)

            with open (f"data/index_page.html",encoding="UTF-8") as file:
                src=file.read() 

            soup=BeautifulSoup(src,"lxml")
            page_count=soup.find("a",class_="pagination__item pagination__item_last pagination-js").text
        except Exception as e:
            print(e)
            page_count=1


        games=[]

        for i in range(1,int(page_count)+1): 
            print(f"Pasring {1} of {int(page_count)+1}")
            page_url=url=url+f"PAGEN_1={i}"
            req=requests.get(url=page_url,headers=header)

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

