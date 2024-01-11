from typing import List


def test_1():
    assert Solution().garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]) == 21


def test_2():
    assert Solution().garbageCollection(["MMM", "PGM", "GP"], [3, 10]) == 37


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        max_house_position = {
            'M': -1,
            'P': -1,
            'G': -1,
        }
        house_count = {
            'M': 0,
            'P': 0,
            'G': 0,
        }

        for i, g in enumerate(garbage):
            if 'M' in g:
                max_house_position['M'] = i

            if 'P' in g:
                max_house_position['P'] = i

            if 'G' in g:
                max_house_position['G'] = i

            for c in g:
                if 'M' == c:
                    house_count['M'] += 1
                if 'P' == c:
                    house_count['P'] += 1
                if 'G' == c:
                    house_count['G'] += 1

        m_time = 0
        p_time = 0
        g_time = 0
        for i, t in enumerate(travel):
            if i < max_house_position['M']:
                m_time += t

            if i < max_house_position['P']:
                p_time += t

            if i < max_house_position['G']:
                g_time += t

        return sum([m_time, p_time, g_time, house_count['M'], house_count['P'], house_count['G']])

