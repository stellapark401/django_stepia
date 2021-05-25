class Wikipedia(object):
    url = ''
    instance_cnt = 0

    def __init__(self):
        self.ins_cnt = Wikipedia.instance_cnt
        Wikipedia.instance_cnt += 1

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        wk = list()
        cnt = 0
        while True:
            menu = int(input('입력\t\t1\n출력\t\t2\n종료\t\t0\n'))
            if menu == 1:
                uV = input('URL 입력: ')
                wk.append(Wikipedia())
                wk[cnt].url = uV
                cnt += 1
            elif menu == 2:
                for i, j in enumerate(wk):
                    print(f'{j.ins_cnt}번 째 URL: {j}')
            elif menu == 0:
                break
            else:
                print('잘못된 입력입니다.')
                continue


Wikipedia.main()
