from typing import List


def test_1():
    assert Solution().findingUsersActiveMinutes([[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], 5) == [0, 2, 0, 0, 0]


def test_2():
    assert Solution().findingUsersActiveMinutes([[1, 1], [2, 2], [2, 3]], 4) == [1, 1, 0, 0]


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_activities = {}
        for user_id, time in logs:
            if user_id not in user_activities:
                user_activities[user_id] = {time}
            else:
                user_activities[user_id].add(time)

        answer = [0 for _ in range(k)]
        for times_set in user_activities.values():
            uam = len(times_set)
            answer[uam - 1] += 1

        return answer
