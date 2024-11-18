# https://leetcode.com/problem-list/sliding-window/url: https://leetcode.com/problems/arithmetic-slices
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 2, n):
                diff = nums[i + 1] - nums[i]
                flag = True
                for k in range(i + 1, j):
                    if nums[k + 1] - nums[k] != diff:
                        flag = False
                        break
                if flag:
                    count += 1

        return count
