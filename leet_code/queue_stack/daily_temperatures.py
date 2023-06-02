from typing import List


def test_main_1():
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    assert Solution().dailyTemperatures(temperatures) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_main_2():
    temperatures = [76, 73]
    assert Solution().dailyTemperatures(temperatures) == [0, 0]


def test_main_3():
    temperatures = [30, 60]
    assert Solution().dailyTemperatures(temperatures) == [1, 0]


def test_main_4():
    temperatures = [30, 60, 90]
    assert Solution().dailyTemperatures(temperatures) == [1, 1, 0]


def test_main_5():
    temperatures = [30, 40, 50, 60]
    assert Solution().dailyTemperatures(temperatures) == [1, 1, 1, 0]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans


class Solution_2:
    def _find_steps(self, current_temperature: int, temperatures: List[int]):
        steps = 1

        for temperature in temperatures:
            if temperature > current_temperature:
                return steps
            steps += 1

        # Не нашли
        return 0

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        for i, temperature in enumerate(temperatures):
            steps = self._find_steps(temperature, temperatures[i + 1:])

            answer.append(steps)

        return answer
