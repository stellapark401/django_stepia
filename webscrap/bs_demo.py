from bs4 import BeautifulSoup


class BsDemo(object):
    html_doc = ''

    def __str__(self):
        return self.html_doc

    @staticmethod
    def main():
        while True:
            menu = int(input('-Input\t\t\t1\n-Read all\t\t2\n-Read title\t\t3\n-Exit\t\t\t0'))
            if menu == 1:
                bsd = BsDemo()
                bsd.html_doc = """<html><head><title>The Dormouse's story</title></head>
                                <body>
                                <p class="title"><b>The Dormouse's story</b></p>
                                
                                <p class="story">Once upon a time there were three little sisters; and their names were
                                <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                                and they lived at the bottom of a well.</p>
                                
                                <p class="story">...</p>
                                """
            elif menu == 2:
                soup = BeautifulSoup(bsd.html_doc, 'html.parser')
                print(soup.prettify())
            elif menu == 3:
                soup = BeautifulSoup(bsd.html_doc, 'html.parser')
                print(soup.find_all('a'))
            elif menu == 0:
                break
            else:
                print('Please choose appropriate menu number.')
                continue


BsDemo.main()
