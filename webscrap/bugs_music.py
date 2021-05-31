from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


class BugsMusic(object):
    url = ''
    rank_dict = dict()
    df_src_index = []

    @classmethod
    def get_ranks(cls, url):
        soup = BeautifulSoup(urlopen(url), 'lxml')
        BugsMusic.rank_dict['title'] = []
        BugsMusic.rank_dict['artist'] = []
        for link in soup.find('div', id='CHARTrealtime').find('tbody').find_all('tr'):
            temp = link.find('div', {'class': 'ranking'}).find('strong').text
            BugsMusic.df_src_index.append(f'{temp}위')
            BugsMusic.rank_dict['artist'].append(link.find('p', {'class': 'artist'}).find('a').text)
            BugsMusic.rank_dict['title'].append(link.find('p', {'adult_yn': "N", 'class': "title"}).find('a').text)

    @staticmethod
    def search_rank():
        search = int(input('몇 위?: ')) - 1
        print(f'{search + 1}위 곡: \'{BugsMusic.rank_dict[search][0]}\'(이)가 부른 \'{BugsMusic.rank_dict[search][1]}\'')

    @staticmethod
    def form_df():
        df = pd.DataFrame(BugsMusic.rank_dict, index=BugsMusic.df_src_index)
        print(df)
        df.to_csv('./data.bugs.csv', sep=',', na_rep='NaN')

    @staticmethod
    def main():
        while True:
            menu = int(input("Input the url\t\t1\nGet ranks\t\t\t2\nSearch rank\t\t\t"
                             "3\nForm a dataframe\t4\nExit\t\t\t\t0"))
            if menu == 1:
                BugsMusic.url = input('URL 입력: ')
            elif menu == 2:
                BugsMusic.get_ranks(BugsMusic.url)
            elif menu == 3:
                BugsMusic.search_rank()
            elif menu == 4:
                BugsMusic.form_df()
            elif menu == 0:
                break
            else:
                print('입력이 바르지 않습니다.')
                continue


BugsMusic.main()
