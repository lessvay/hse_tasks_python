# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=problem-list-v2&envId=array&status=SOLVED
import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        res = []
        pq = []

        for num in nums1:
            heapq.heappush(pq, (num + nums2[0], 0))

        while k > 0 and pq:
            sum_, j = heapq.heappop(pq)
            res.append([sum_ - nums2[j], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(pq, (sum_ - nums2[j] + nums2[j + 1], j + 1))

            k -= 1

        return res
