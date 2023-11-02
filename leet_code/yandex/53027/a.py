import sys
import uuid
from pathlib import Path
from typing import List, Optional


def read_from_file(file_name: Optional[str] = 'input.txt', base_dir: Optional[str] = None) -> List[List[str]]:
    result = []
    if base_dir:
        file_name = Path(base_dir) / file_name
    with open(file_name, 'r', encoding='UTF-8') as reader:
        while line := reader.readline():
            line = line.strip()
            if line:
                result.append(line.split(' '))
    return result


def write_to_file(lines: List[str], file_name: Optional[str] = None, file_prefix: Optional[str] = None,
                  base_dir: Optional[str] = None):
    if not file_name:
        file_name = f'{str(uuid.uuid4().hex)[:6]}.txt'

    if file_prefix:
        file_name = f'{file_prefix}_{file_name}'

    if base_dir:
        file_name = Path(base_dir) / file_name

    with open(file_name, 'w', encoding='UTF-8') as writer:
        for i, line in enumerate(lines):
            if i == len(lines) - 1:
                writer.write(f'{line}')
            else:
                writer.write(f'{line}\n')


def main(data):
    answer = []
    if len(data) >= 3:
        nums = list(map(int, data[1]))

        for start, stop in data[2:]:
            start, stop = int(start), int(stop)
            sub_nums = nums[start: stop + 1]
            found = False
            for i in range(len(sub_nums) - 1):
                next_i = i + 1
                cur = sub_nums[i]
                next_item = sub_nums[next_i]
                if next_item > cur:
                    answer.append(str(next_item))
                    found = True
                    break

            if not found:
                answer.append('NOT FOUND')

    return answer


# def test_1():
#     main([[10, 5],
#           [1, 1, 1, 2, 2, 2, 3, 3, 3, 10],
#           [0, 1]])


if __name__ == '__main__':
    write_to_file(lines=main(read_from_file()), file_name='output.txt')
