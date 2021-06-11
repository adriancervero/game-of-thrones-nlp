"""
    Scraps user ratins for each episode of Game of Thrones
    from IMDB (https://www.imdb.com/)

    Returns pandas dataframe

"""

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

N_SEASONS = 8

ratings = {
    'episode_name':[],
    'rate': []
}

for i in range(1, N_SEASONS+1):
    print('\nSEASON', i)

    url = f'https://www.imdb.com/title/tt0944947/episodes?season={i}'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    ep_list = soup.find_all('div', class_='info')
    
    for episode in ep_list:
        episode_name = episode.find('a', itemprop="name").text
        rate = episode.find('span', class_='ipl-rating-star__rating').text
        #print(episode_name, rate)

        ratings['episode_name'].append(episode_name)
        ratings['rate'].append(rate)

ratings = pd.DataFrame(ratings)
ratings.to_csv('../../data/raw/ratings.csv', index=False)
