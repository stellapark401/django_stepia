class Gugudan(object):
    dan = 0

    def print_it(self):
        print('=' * 20)
        if self.dan <= 9:
            for i in range(9):
                print(f'\t{self.dan} x {i + 1} = {self.dan * (i + 1)}')
        else:
            for i in range(self.dan):
                print(f'\t{self.dan} x {i + 1} = {self.dan * (i + 1)}')

    def print_all(self):
        for i in range(1, 9):
            self.dan = i + 1
            self.print_it()

    @staticmethod
    def main():
        ggd = Gugudan()
        while True:
            mn = int(input('-구구단 출력\t\t1\n-모든 단 출력\t\t2\n-종료\t\t\t0'))
            if mn == 1:
                ggd.dan = int(input('출력할 단: '))
                ggd.print_it()
            elif mn == 2:
                ggd.print_all()
            elif mn == 0:
                break
            else:
                print('Wrong number')


Gugudan.main()
