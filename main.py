import requests
from bs4 import BeautifulSoup
import json
from Igromagaz import Igromagaz

header={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
my_url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&PAGEN_1=1"

igromagaz=Igromagaz(url=my_url,headers=header)
       

    
def main():
    igromagaz.get_data()


