class VectorTest(object):
    param1 = ''
    param2 = ''

    def create(self, vect_type):
        if vect_type == 'list':
            self.param1.append(self.param2)
            return self.param1
        elif vect_type == 'tuple':
            self.param1 += self.param2,
            return self.param1
        elif vect_type == 'dict':
            self.param1.update(self.param2)
            return self.param1
        elif vect_type == 'set':
            self.param1.add(self.param2)
            return self.param1
        else:
            print('지원하지않는 벡터 타입입니다.')

    def read(self, vect_type):
        if vect_type == 'list':
            print(self.param1)
        elif vect_type == 'tuple':
            print(self.param1)
        elif vect_type == 'dict':
            print(self.param1)
        elif vect_type == 'set':
            print(self.param1)
        else:
            print('지원하지않는 벡터 타입입니다.')

    def vec_update(self, vect_type):
        if vect_type == 'list':
            self.param1 += self.param2
            return self.param1
        elif vect_type == 'tuple':
            self.param1 += self.param2
            print(self.param1)
            return self.param1
        elif vect_type == 'dict':
            self.param1.update(self.param2)
            return self.param1
        elif vect_type == 'set':
            self.param1.update(self.param2)
            return self.param1
        else:
            print('지원하지않는 벡터 타입입니다.')

    def vec_delete(self, vect_type):
        if vect_type == 'list':
            for i, j in enumerate(self.param1):
                if j == self.param2:
                    del self.param1[i]
            return self.param1
        elif vect_type == 'tuple':
            for i, j in enumerate(self.param1):
                if j == self.param2:
                    self.param1 = self.param1[:i] + self.param1[i + 1:]
            return self.param1
        elif vect_type == 'dict':
            del self.param1[self.param2]
            return self.param1
        elif vect_type == 'set':
            self.param1.remove(self.param2)
            return self.param1
        else:
            print('지원하지않는 벡터 타입입니다.')

    @staticmethod
    def select_type(choice):
        if choice == 1:
            return 'list'
        elif choice == 2:
            return 'tuple'
        elif choice == 3:
            return 'dict'
        elif choice == 4:
            return 'set'
        elif choice == 0:
            return 'exit'
        else:
            print('잘못입력하셨습니다.')

    @staticmethod
    def main():
        lst = [1, 2, 3]
        tp = (1, 2, 3)
        dct = {'a': 1, 'b': 2, 'c': 3}
        st = {1, 2, 3}

        vt = VectorTest()
        menu = '-List\t\t1\n-Tuple\t\t2\n-Dictionary\t3\n-Set\t\t4\n-Exit\t\t0'
        while True:
            choice = int(input('+Create\t1\n+Read\t2\n+Update\t3\n+Delete\t4\n+Exit\t0'))
            if choice == 1:
                a = VectorTest.select_type(int(input(menu)))
                if a == 'exit':
                    continue
                elif a == 'list':
                    vt.param1, vt.param2 = lst, 4
                    print(vt.create(a))
                elif a == 'tuple':
                    vt.param1, vt.param2 = tp, 4
                    print(vt.create(a))
                elif a == 'dict':
                    vt.param1, vt.param2 = dct, {'d': 4}
                    print(vt.create(a))
                elif a == 'set':
                    vt.param1, vt.param2 = st, 4
                    print(vt.create(a))
                else:
                    continue
            elif choice == 2:
                a = VectorTest.select_type(int(input(menu)))
                if a == 'exit':
                    continue
                elif a == 'list':
                    vt.param1 = lst
                    print(vt.read(a))
                elif a == 'tuple':
                    vt.param1 = tp
                    print(vt.read(a))
                elif a == 'dict':
                    vt.param1 = dct
                    print(vt.read(a))
                elif a == 'set':
                    vt.param1 = st
                    print(vt.read(a))
                else:
                    continue
            elif choice == 3:
                a = VectorTest.select_type(int(input(menu)))
                if a == 'exit':
                    continue
                elif a == 'list':
                    vt.param1, vt.param2 = lst, [4, 5]
                    print(vt.vec_update(a))
                elif a == 'tuple':
                    vt.param1, vt.param2 = tp, (4, 5)
                    print(vt.vec_update(a))
                elif a == 'dict':
                    vt.param1, vt.param2 = dct, {'d': 4, 'e': 5}
                    print(vt.vec_update(a))
                elif a == 'set':
                    vt.param1, vt.param2 = st, {4, 3, 5}
                    print(vt.vec_update(a))
                else:
                    continue
            elif choice == 4:
                a = VectorTest.select_type(int(input(menu)))
                if a == 'exit':
                    continue
                elif a == 'list':
                    vt.param1, vt.param2 = lst, 2
                    print(vt.vec_delete(a))
                elif a == 'tuple':
                    vt.param1, vt.param2 = tp, 1
                    print(vt.vec_delete(a))
                elif a == 'dict':
                    vt.param1, vt.param2 = dct, 'b'
                    print(vt.vec_delete(a))
                elif a == 'set':
                    vt.param1, vt.param2 = st, 2
                    print(vt.vec_delete(a))
                else:
                    continue
            elif choice == 0:
                break
            else:
                print('Wrong number')


VectorTest.main()
