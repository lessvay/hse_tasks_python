# https://leetcode.com/problems/arithmetic-slices/description/?envType=problem-list-v2&envId=sliding-window
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        ans = 0
        for i in range(0, len(nums) - 2):
            curr = nums[i : i + 3]
            if curr[1] - curr[0] == curr[2] - curr[1]:
                ans += 1
                for j in range(i + 3, len(nums)):
                    curr.append(nums[j])
                    if curr[1] - curr[0] == curr[-1] - curr[-2]:
                        ans += 1
                    else:
                        break
        return ans
