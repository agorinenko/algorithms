import operator
import random
from dataclasses import dataclass
from typing import Callable, List

SIGNS = [operator.add, operator.sub]
FIRST_LIM = [1, 10]
SECOND_LIM = [1, 10]
WITH_ANSWERS = False
ALLOW_ZERO_ANSWERS = False
ALLOW_DUPLICATE = False
TOTAL_COUNT = 28


@dataclass
class Example:
    first: int
    second: int
    sign: Callable

    @property
    def answer(self) -> int:
        return self.sign(self.first, self.second)

    def __str__(self):
        sign = '-' if self.sign == operator.sub else '+'
        if WITH_ANSWERS:
            return f'{self.first}{sign}{self.second}={self.answer}'

        return f'{self.first}{sign}{self.second}='

    def __eq__(self, other: 'Example'):
        return self.first == other.first and self.second == other.second and self.sign == other.sign


def generate_example(examples: List[Example]) -> Example:
    first = random.randint(*FIRST_LIM)
    second = random.randint(*SECOND_LIM)
    sign = SIGNS[random.randint(0, 1)]

    if sign == operator.sub and second > first:
        second, first = first, second

    example = Example(first=first, second=second, sign=sign)
    if not ALLOW_ZERO_ANSWERS and example.answer == 0:
        example = generate_example(examples)
    elif not ALLOW_DUPLICATE and examples and examples[-1] == example:
        example = generate_example(examples)

    return example


if __name__ == '__main__':
    i = TOTAL_COUNT
    _examples = []
    for _ in range(i):
        _examples.append(generate_example(_examples))

    assert len(_examples) == i

    for _example in _examples:
        print(str(_example))
        print('---------')
