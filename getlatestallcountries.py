import requests
import pandas as pd
url = "https://covid-193.p.rapidapi.com/countries"

headers = {
	"x-rapidapi-key": "45233d523amsh8aa1255e7fc05c5p19bd71jsn0569323d3802",
	"x-rapidapi-host": "covid-193.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

df=pd.DataFrame(response.json()['response'])
print(df)