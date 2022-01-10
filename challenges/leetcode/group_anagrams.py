"""
Solution for LC#49: Group Anagrams

https://leetcode.com/problems/group-anagrams/
"""
from typing import Dict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: Dict[str, List[str]] = dict()  # dict[sorted_s] : [anagrams that lead to same sorted_s]

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s] = []

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)

        return [anagram for anagram in anagrams.values()]
