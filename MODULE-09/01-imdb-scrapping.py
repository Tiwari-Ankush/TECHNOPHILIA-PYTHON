
print('''

IMDB DATA EXTRACTION USING BEAUTIFUL SOUP >>
''')

from bs4 import BeautifulSoup
import pandas as pd

# df = pd.read_csv("./MODULE-09/links.csv")
# print(df.head())

def get_movie_id(num=20,page=1):
    links_data=pd.read_csv("./MODULE-09/links.csv")
    movie_ids = list(links_data.imdbId)
    start_index=(page-1)*num
    end_index = start_index+num
    return movie_ids[start_index:end_index]

if __name__== "__main__":
    ids= get_movie_id(10)
    print(ids)