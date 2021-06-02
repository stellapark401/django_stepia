print(range(3))


def positive(x):
    return x > 0


print(filter(positive, [1, -3, 2, 0, -5, 6]))


def fn_1(a, b, c):
    print(a, b, c)


tp = (1, 2, 3)

fn_1(*tp)


def fn_2(param):
    return param == 'a'


print(list(map(fn_2, ['a', 'b', 'c'])))
print(zip('a', 'b', 'c'))
print(type(zip('a', 'b', 'c')))
print(list(zip('a', 'b', 'c')))

for i in zip('a', 'b', 'c'):
    print(i)

for i in map(fn_2, ['a', 'b', 'c']):
    print(i)

for i in filter(positive, [1, -3, 2, 0, -5, 6]):
    print(i)


def fn_3(**dct):
    if dct['a']:
        print(dct['b'])
    else:
        print('Printing null')


fn_3(a=True, b=22)
fn_3(a=False, b=33)
