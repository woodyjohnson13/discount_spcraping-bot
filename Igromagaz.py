from Getter import Getter
import json
import requests
from bs4 import BeautifulSoup


class Igromagaz(Getter):


    def get_data(url,headers):
        #req=requests.get(url=url,headers=headers)
    
        #with open(f"data/index_page.html","w",encoding="UTF-8") as file:
            #file.write(req.text)

        #with open (f"data/index_page.html",encoding="UTF-8") as file:
            #src=file.read() 

        #soup=BeautifulSoup(src,"lxml")
        #page_count=soup.find("a",class_="pagination__item pagination__item_last pagination-js")
            games=[]
            for i in range(1,2): #int(page_count)+1
                #req=requests.get(url=url)

                #with open(f"data/index_{i}.html","w",encoding="UTF-8") as file:
                    #file.write(req.text)

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
                        #print("https://www.igromagaz.ru"+ref)
                        #print(name.text.replace(" (ключ для ПК)",""))
                        #print(old_price.text.strip().replace(" руб.","")+"/"+new_price.text)
                        games.append({
                            "Название":name.text.replace(" (ключ для ПК)",""),
                            "Цена":(old_price.text.strip().replace(" руб.","")+"/"+new_price.text),
                            "Cсылка":"https://www.igromagaz.ru"+ref
                        })
                    except Exception as e:
                        print(e)
                        continue


            with open("igromagaz_discount.json","w",encoding="UTF-8") as file:
                json.dump(games,file,indent=4,ensure_ascii=False)

