from sheck import num


def test_num(n,expect):
    if num(n) != expect:
        print('ERROR')
