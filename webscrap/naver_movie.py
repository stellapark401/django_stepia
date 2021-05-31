from selenium import webdriver
import pandas as pd


class NaverMovie(object):
    df_src_index = []
    df_src = {'title': []}
    url = ''
    classes = []
    # 객체의 디폴트는 None 으로 잡는다.
    driver = None
    df = None

    @staticmethod
    def main():

        driver = webdriver.Chrome()

        while True:
            mn = int(input('-set the url\t\t\t1\n-get the ranks\t\t\t2\n-form a dataframe\t\t3\n-click to another page'
                           '\t4\n-exit\t\t\t\t\t0'))
            if mn == 1:
                NaverMovie.url = input('input rul: ')
                driver.get(NaverMovie.url)
            elif mn == 2:
                temp = driver.find_elements_by_class_name('title')
                for i, v in enumerate(temp):
                    NaverMovie.df_src_index.append(f'{i + 1}위')
                    NaverMovie.df_src['title'].append(v.find_element_by_tag_name('a').text)
            elif mn == 3:
                NaverMovie.df = pd.DataFrame(NaverMovie.df_src, index=NaverMovie.df_src_index)
                print(NaverMovie.df)
                NaverMovie.df.to_csv('./data.naver_movie.csv')
            elif mn == 4:
                driver.find_element_by_link_text('평점순(현재상영영화)').click()
            elif mn == 0:
                break
            else:
                print('Wrong menu')


NaverMovie.main()
