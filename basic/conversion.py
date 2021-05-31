import pandas as pd


class Conversion(object):
    @staticmethod
    def create_tuple() -> ():
        return tuple(range(1, 11))

    @staticmethod
    def to_lst_int(tp) -> []:
        return list(tp)

    @staticmethod
    def to_float(lst) -> []:
        return [float(i) for i in lst]

    @staticmethod
    def back_to_lst(lst) -> []:
        return [int(f) for f in lst]

    @staticmethod
    def to_dict(lst) -> {}:
        temp = {}
        for i, v in enumerate(lst):
            temp[str(i)] = v
        return temp

    @staticmethod
    def to_tp(st) -> ():
        return tuple(st)

    @staticmethod
    def to_lst_cha(tp) -> []:
        return list(tp)

    @staticmethod
    def to_dataframe(dt):
        df_src = {}
        for k, v in dt.items():
            df_src[k] = list((v, ))
        return pd.DataFrame(df_src)

    @staticmethod
    def main():
        i = 0
        f = 0.0
        st = 'hello'
        lst_int = []
        lst_float = []
        tp_int = ()
        tp_cha = ()
        dt = {}
        df = pd.DataFrame()
        cvs = Conversion()
        print(type(df))
        while True:
            mn = int(input('-create tuple\t\t1\n-to integer list\t2\n-to float\t\t\t3\n'
                           '-to integer\t\t\t4\n-to dictionary\t\t5\n-to tuple\t\t\t6\n'
                           '-to character list\t7\n-to dataframe\t\t8\n-exit\t\t\t\t0'))
            if mn == 1:
                tp_int = cvs.create_tuple()
                print(tp_int)
            elif mn == 2:
                lst_int = cvs.to_lst_int(tp_int)
                print(lst_int)
            elif mn == 3:
                lst_float = cvs.to_float(lst_int)
                print(lst_float)
            elif mn == 4:
                lst_int = cvs.back_to_lst(lst_float)
                print(lst_int)
            elif mn == 5:
                dt = cvs.to_dict(lst_int)
                print(dt)
            elif mn == 6:
                tp_cha = cvs.to_tp(st)
                print(tp_cha)
            elif mn == 7:
                lst_cha = cvs.to_lst_cha(tp_cha)
                print(lst_cha)
            elif mn == 8:
                df = cvs.to_dataframe(dt)
                print(df)
            elif mn == 0:
                break
            else:
                print('Wrong number')


Conversion.main()
