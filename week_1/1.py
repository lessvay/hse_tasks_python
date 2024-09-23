
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=problem-list-v2&envId=string
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keyboard = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": " "
        }

        if not digits:
            return []

        res = [""]  

        for digit in digits:
            letters = keyboard[digit]  
            temp_res = []  

            for combination in res:
                for letter in letters:
                    temp_res.append(combination + letter)  

            res = temp_res  

        return res




