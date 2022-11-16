import requests
from bs4 import BeautifulSoup
import json
from Igromagaz import Igromagaz


my_url="https://www.igromagaz.ru/igry-dlya-pc/?activations%5B31903%5D=31903&discount_percent=Y&PAGEN_1=1"

igromagaz=Igromagaz()
       

    
def main():
    igromagaz.get_data()


