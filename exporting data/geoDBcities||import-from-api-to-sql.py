
# api from rapid api   'https://rapidapi.com/wirefreethought/api/geodb-cities/playground/apiendpoint_f4626780-d13b-443e-8a21-0169642b7d5a'
import requests

url = "https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions"

headers = {
    "X-RapidAPI-Key": "b0f75c828fmsh2b0480a62ab8d23p18178ajsn3267e033ae6a",
    "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

data = response.json()['data']
links = response.json()['links']
metadata = response.json()['metadata']

next_url=links[1]['href']
# print(next_url)

count=metadata['totalCount']//5
# print(count)

# print(links)

import time

import time


for i in range(1,count):
    
    
    url = "https://wft-geo-db.p.rapidapi.com"
    page = url + next_url
    
    response = requests.request("GET", page, headers=headers)
    
    print(response.json())
    
    links = response.json()['links']
    
    for item in links:
        if item['rel'] == 'next':
            next_url = item['href']
            
    data.extend(response.json()['data'])
    
    time.sleep(2)

import pandas as pd
import pymysql
cities=pd.DataFrame()

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:@localhost/temp_db")
# engine = create_engine("mysql+pymysql://{username}:{password}@localhost/{databasename}}")
cities.to_sql("cities",con=engine,if_exists='append')