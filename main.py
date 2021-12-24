def test():
    assert (main(1, 1, '-') == 0)
    assert (main(-1, 1, '+') == 0)
    assert (main(2, 7, '*') == 14)
    assert (main(8, 2, '/') == 4)
    print('All tests passed')


def main(a, b, sign):
    if sign == '-':
        return a - b
    elif sign == '+':
        return a + b
    elif sign == '*':
        return a * b
    elif sign == '/':
        return a / b


if __name__ == '__main__':
    test()
