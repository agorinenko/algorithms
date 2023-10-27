import random

if __name__ == '__main__':
    i = 50
    signs = ['+', '-']
    first_lim = [1, 20]
    second_lim = [1, 10]
    for _ in range(i):
        first = random.randint(*first_lim)
        second = random.randint(*second_lim)
        sign = signs[random.randint(0, 1)]
        if sign == 1 and second > first:
            second, first = first, second

        print(f'{first}{sign}{second}=')
        print('---------')
