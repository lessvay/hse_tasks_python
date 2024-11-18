# https://leetcode.com/problem-list/sliding-window/url: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        dq = deque()
        sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            sums[i + 1] = sums[i] + nums[i]
        min_length = 100001
        for i in range(len(sums)):
            while dq and sums[i] - sums[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            while dq and sums[i] <= sums[dq[-1]]:
                dq.pop()
            dq.append(i)

        if min_length != 100001:
            return min_length
        else:
            return -1
