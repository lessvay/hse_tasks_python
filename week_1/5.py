# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=string
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = []
        max_len = 0
        
        for i in s:
            if i in substring:
                substring = substring[substring.index(i)+1:]
            
            substring.append(i)
            max_len = max(max_len, len(substring))
        
        return max_len
        

