"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/replace-the-substring-for-balanced-string/
"""


class Solution:
    def balancedString(self, s: str) -> int:
        target = len(s) // 4
        count = {"Q": 0, "W": 0, "E": 0, "R": 0}
        for char in s:
            count[char] += 1
        if all(c <= target for c in count.values()):
            return 0
        left = 0
        mn = len(s)
        for right in range(len(s)):
            count[s[right]] -= 1
            while all(count[c] <= target for c in count):
                mn = min(mn, right - left + 1)
                count[s[left]] += 1
                left += 1

        return mn
