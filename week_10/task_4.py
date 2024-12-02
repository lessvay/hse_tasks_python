# leetcode.com/problem-list/sliding-window/url: https://leetcode.com/problems/jump-game-vii/description/?envType=problem-list-v2&envId=sliding-window
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == "1":
            return False
        n = len(s)
        arr = [False] * n
        arr[0] = True
        max_pos = minJump
        for i in range(n):
            if arr[i]:
                min_pos = max(i + minJump, max_pos)
                max_pos = min(i + maxJump + 1, n)
                for j in range(min_pos, max_pos):
                    if s[j] == "0":
                        arr[j] = True
                if max_pos == n:
                    return arr[-1]
        return arr[-1]
