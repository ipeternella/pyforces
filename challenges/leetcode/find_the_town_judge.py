"""
Solution for LC#997: Find the Town Judge

https://leetcode.com/problems/find-the-town-judge/
"""
from typing import Dict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        believers = set()
        trusts: Dict[int, int] = dict()
        judge = -1

        if not trust:
            return 1 if n == 1 else -1  # city with just the judge

        for has_trust, trusted in trust:
            believers.add(has_trust)
            trusts[trusted] = trusts.get(trusted, 0) + 1

        for trusted_person, amount in trusts.items():
            if amount == n - 1:  # max trust amount required by a judge
                if judge == -1:
                    judge = trusted_person
                else:
                    return -1  # no possible judges

        return judge if judge not in believers else -1
