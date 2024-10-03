from bs4 import BeautifulSoup
import requests


webpage=requests.get('https://www.flipkart.com/search?q=smartphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT&suggestionId=smartphone%7CMobiles&requestId=88e9e105-46d3-48e8-ae92-2413b381bd6d&as-searchtext=smart&page=1').text

soup=BeautifulSoup(webpage,'lxml')

div=soup.find('div', class_='cPHDOP col-12-12')
print(webpage)
