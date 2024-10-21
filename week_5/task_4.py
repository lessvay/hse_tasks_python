# https://leetcode.com/problems/majority-element-ii/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM%2CHARD
from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]):
        element_count = Counter(nums)

        majority_elements = []
        threshold = len(nums) // 3

        for element, count in element_count.items():
            # Check if the element count is greater than the threshold
            if count > threshold:
                majority_elements.append(element)

        return majority_elements
