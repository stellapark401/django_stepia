from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):
    url = ''
    rank_dict = dict()

    @staticmethod
    def get_ranks(url):
        soup = BeautifulSoup(urlopen(url), 'lxml')
        for link in soup.find_all(name='tr', attrs={'rowtype': 'track'}):
            rank = int(link.find('div', {'class': 'ranking'}).find('strong').text) - 1
            BugsMusic.rank_dict[rank] = (link.find('p', {'class': 'artist'}).find('a').text, link.find('p', {'class': 'title'}).find('a').text)
        if len(BugsMusic.rank_dict) == 100:
            print('100위까지 차트를 읽어왔습니다.')
        else:
            print('다시 시도해주세요.')

    @staticmethod
    def search_rank():
        search = int(input('몇 위?: ')) - 1
        print(f'{search + 1}위 곡: \'{BugsMusic.rank_dict[search][0]}\'(이)가 부른 \'{BugsMusic.rank_dict[search][1]}\'')

    @staticmethod
    def main():
        while True:
            menu = int(input("Input the url\t1\nGet ranks\t\t2\nSearch rank\t\t3\nExit\t\t\t0"))
            if menu == 1:
                BugsMusic.url = input('URL 입력: ')
            elif menu == 2:
                BugsMusic.get_ranks(BugsMusic.url)
            elif menu == 3:
                BugsMusic.search_rank()
            elif menu == 0:
                break
            else:
                print('입력이 바르지 않습니다.')
                continue


BugsMusic.main()
