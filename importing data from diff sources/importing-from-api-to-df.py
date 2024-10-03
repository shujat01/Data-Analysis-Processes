import pandas as  pd 
import numpy as numpy
import requests


response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=3b7575dd39ef40ac1627b8c69ff9f9c4&language=en-US&page=1')
response.json()['results']
# ['adult', 'backdrop_path', 'genre_ids', 'id', 'original_language',
#        'original_title', 'overview', 'popularity', 'poster_path',
#        'release_date', 'title', 'video', 'vote_average', 'vote_count']
new_df=pd.DataFrame()
for i in range(1,21):
    response=requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=3b7575dd39ef40ac1627b8c69ff9f9c4&language=en-US&page={}'.format(i))
    temp_df = pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]
    new_df = pd.concat([temp_df],ignore_index=True)
    

new_df.to_csv('tempmovies.csv')
print(new_df)