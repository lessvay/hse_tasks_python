class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        n = len(nums)
        ans = float("inf")

        for i in range(n):
            sum = 0

            for j in range(i, n):
                sum += nums[j]

                if sum >= target:
                    ans = min(ans, j - i + 1)
                    break

        return 0 if ans == float("inf") else ans
