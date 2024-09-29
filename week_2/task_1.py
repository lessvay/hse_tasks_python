# https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=string
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        Roman = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        number_of_tens = 0
        roman_string = ""
        while num > 0:
            current_number = num % 10
            if current_number == 4 or current_number == 9:
                roman_string = Roman[current_number * 10**number_of_tens] + roman_string
            else:
                if current_number < 5:
                    roman_string = (
                        Roman[10**number_of_tens] * current_number + roman_string
                    )
                else:
                    roman_string = (
                        Roman[5 * 10**number_of_tens]
                        + Roman[10**number_of_tens] * (current_number % 5)
                        + roman_string
                    )
            number_of_tens += 1
            num = num // 10

        return roman_string
