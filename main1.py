total = 0


def foo():
    global total
    total = 1


if __name__ == '__main__':
    print(total)
