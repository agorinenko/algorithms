def test_main_1():
    assert Solution().romanToInt('LVIII') == 58

def test_main_2():
    assert Solution().romanToInt('MCMXCIV') == 1994


class Solution:
    def romanToInt(self, s: str) -> int:
        int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        skip_next = False
        for i, simbol in enumerate(s):
            if skip_next:
                skip_next = False
                continue

            if i != len(s) - 1:
                next_simbol = s[i + 1]
                if simbol == 'I' and next_simbol == 'V':
                    sum += 4
                    skip_next = True
                    continue

                if simbol == 'I' and next_simbol == 'X':
                    sum += 9
                    skip_next = True
                    continue

                if simbol == 'X' and next_simbol == 'L':
                    sum += 40
                    skip_next = True
                    continue

                if simbol == 'X' and next_simbol == 'C':
                    sum += 90
                    skip_next = True
                    continue

                if simbol == 'C' and next_simbol == 'D':
                    sum += 400
                    skip_next = True
                    continue

                if simbol == 'C' and next_simbol == 'M':
                    sum += 900
                    skip_next = True
                    continue


            if simbol in int_map:
                sum += int_map[simbol]

        return sum
