if __name__ == '__main__':
    reader = open('input.txt', 'r')
    lines = reader.readlines()
    reader.close()
    input_str = ''.join(lines).replace(' ', '').replace('\n', '')

    c_map = {}
    for c in input_str:
        if c in c_map:
            c_map[c] += 1
        else:
            c_map[c] = 1

    c_list = sorted(list(c_map.keys()))
    c_max_count = max(list(c_map.values()))
    current_row = 1

    for i in range(c_max_count):
        print_chars = []
        for c in c_list:
            c_num = c_map[c]
            # Сколько пропустить
            j = c_max_count - c_num
            if current_row > j:
                print_chars.append('#')
            else:
                print_chars.append(' ')

        print(''.join(print_chars))
        current_row += 1

    print(''.join(c_list))
