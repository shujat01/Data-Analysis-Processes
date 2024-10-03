import requests
from bs4 import BeautifulSoup
import time


import pandas as pd
import numpy as np 

webpage=requests.get('https://www.flipkart.com/search?q=smartphones&page=1').text
soup=BeautifulSoup(webpage,'lxml')
all_divs=soup.find_all('div',class_="tUxRFH")
print(all_divs)
