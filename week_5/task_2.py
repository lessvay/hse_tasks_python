# https://leetcode.com/problems/group-anagrams/solutions/4025789/easy-python-solution-briefly-explained/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM%2CHARD
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]):
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)

        return ans.values()
