# https://leetcode.com/problems/largest-number/?envType=problem-list-v2&envId=array&status=SOLVED
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key

        def compare(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1

        str_nums = list(map(str, nums))

        str_nums.sort(key=cmp_to_key(compare))

        if str_nums[0] == "0":
            return "0"

        return "".join(str_nums)
