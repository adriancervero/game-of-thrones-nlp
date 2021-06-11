"""
    Script that scrap Genius website to extract
    Game of Thrones script using BeautifulSoup and requests
"""

import requests
from bs4 import BeautifulSoup
import time

N_SEASONS = 8


with open('../../data/raw/script_raw.txt', 'w') as f:

    for i in range(1, N_SEASONS+1):

        url = f'https://genius.com/albums/Game-of-thrones/Season-{i}-scripts'

        r = requests.get(url)
        soup_season = BeautifulSoup(r.text, 'html.parser')
        print('\nSEASON', i)
        f.write(f'\nSEASON {i}\n')
        

        for idx, titles in enumerate(soup_season.find_all(class_='chart_row-content-title')):
            episode_title = titles.text.strip().split('\n')[0]
            episode_title = episode_title.lower().replace(' ', '-').replace(',', '').replace("'", "")
            

            episode_url = f'https://genius.com/Game-of-thrones-{episode_title}-annotated'

            print(f'episode {idx+1:01d}: {episode_title}')
            successfull = False
            while not successfull:
                try:
                    r2 = requests.get(episode_url)
                    soup_episode = BeautifulSoup(r2.text, 'html.parser')
                    paragraphs = soup_episode.find('div', class_='lyrics').find_all('p')
                    successfull = True
                except AttributeError:
                    time.sleep(3)
                

            script_string = '\n'.join([p.text for p in paragraphs])
            f.write('\n'+script_string)
            
        
            

        

    