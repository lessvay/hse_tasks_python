# leetcode.com/problem-list/sliding-window/https://leetcode.com/problems/minimum-size-subarray-sum/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        start = 0
        curr_sum = 0
        min_l = 10**9

        for end in range(n):
            curr_sum += nums[end]
            while curr_sum >= target:
                min_l = min(min_l, end - start + 1)
                curr_sum -= nums[start]
                start += 1

        return min_l if min_l != 10**9 else 0
