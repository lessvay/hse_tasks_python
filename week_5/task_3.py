# https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM%2CHARD
class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        s += (num // 1000) * "M"
        num -= (num // 1000) * 1000
        if num // 500 == 1:
            if num // 100 == 9:
                s += "CM"
            else:
                s += "D" + "C" * ((num // 100) - 5)
        else:
            if num // 100 == 4:
                s += "CD"

            else:
                s += "C" * (num // 100)
        num -= (num // 100) * 100
        if num // 50 == 1:
            if num // 10 == 9:
                s += "XC"
            else:
                s += "L" + "X" * ((num // 10) - 5)
        else:
            if num // 10 == 4:
                s += "XL"
            else:
                s += "X" * (num // 10)
        num -= (num // 10) * 10
        if num // 5 == 1:
            if num // 1 == 9:
                s += "IX"
            else:
                s += "V" + "I" * ((num // 1) - 5)
        else:
            if num // 1 == 4:
                s += "IV"
            else:
                s += "I" * (num // 1)
        return s
