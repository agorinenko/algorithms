import sys
import uuid
from pathlib import Path
from typing import Optional, List


def read_from_stdout() -> List[List[str]]:
    result = []

    while line := input():
        line = line.strip()
        if line:
            result.append(line.split(' '))
    return result


def write_to_stdout(lines: List[str]):
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            sys.stdout.write(f'{line}')
        else:
            sys.stdout.write(f'{line}\n')


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
