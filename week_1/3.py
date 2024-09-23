# https://leetcode.com/problems/compare-version-numbers/description/?envType=problem-list-v2&envId=string
class Solution(object):
    numbers = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}

    def string_to_int(self, split):
        split_len = len(split)
        result = 0
        for i in split:
            split_len -= 1
            result += self.numbers[i] * (10 ** (split_len))
        return result

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_split = version1.split(".")
        version2_split = version2.split(".")

        length = max(len(version1_split), len(version2_split))
        
        version1_split += ["0"] * (length - len(version1_split))
        version2_split += ["0"] * (length - len(version2_split))

        for split1, split2 in zip(version1_split, version2_split):
            int1 = self.string_to_int(split1)
            int2 = self.string_to_int(split2)
            if int1 > int2:
                return 1
            if int1 < int2:
                return -1
        return 0
