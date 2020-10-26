import requests
from bs4 import BeautifulSoup

URL1 = 'https://www.tiendasjumbo.co/televisor-lg-55-oled-uhd-4k-oled55b9pd-20044359/p'
URL2 = 'https://www.alkosto.com/televisor-55-139-cm-oled-lg-oled55b8sdc-uhd-4k-smart-tv'
URL3 = "https://www.ktronix.com/tv-lg-55-pulgadas-139-cm-oled55b8sdc-uhd-4k-oled-plano-smart-tv/p/8806098280100"
URL4 = "https://www.alkosto.com/tv-lg-55-pulgadas-139-cm-oledb9-4k-uhd-smart-tv"
URL5 = "https://www.ktronix.com/tv-lg-55-pulgadas-139-cm-55b9-oled-4k-uhd-smart-tv/p/8806098460687"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}

def checkpriceJumbo(URL):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(class_ ="skuBestPrice").get_text()

    converted_price = float(price[1]+price[3:6]+price[7:10])
    print (converted_price)

    
def checkpriceAlkosto(URL):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser',from_encoding="iso-8859-1")

    price = soup.find("span", itemprop="price").get_text()

    converted_price = float(price[0]+price[2:5]+price[6:9])
    print (converted_price)

def checkpriceKatronix(URL):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser',from_encoding="iso-8859-1")

    price = soup.find(class_="price-ktronix").get_text().strip()

    converted_price = float(price[1]+price[3:6]+price[7:10])
    
    print (converted_price)

checkpriceJumbo(URL1)

checkpriceAlkosto(URL2)
checkpriceAlkosto(URL4)

checkpriceKatronix(URL3)
checkpriceKatronix(URL5)
