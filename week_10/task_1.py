# leetcode.com/problem-list/sliding-windowurl: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
class Solution:
    def maxScore(self, cardPoints: list[int], K: int) -> int:
        n = len(cardPoints)
        score = sum(cardPoints)
        win = sum(cardPoints[: n - K])
        ans = win

        for right in range(n - K, n):
            win = win - cardPoints[right - n + K] + cardPoints[right]
            ans = min(ans, win)

        return score - ans
