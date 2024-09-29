# https://leetcode.com/problems/integer-to-english-words/description/?envType=problem-list-v2&envId=string&status=SOLVED
class Solution(object):
    Words = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion",
    }

    def number_to_thousands(self, num):
        thousands = []
        number_of_thousands = 0

        while num > 0:
            current_number = num % 1000
            if current_number > 0:
                thousands.append(
                    {
                        "current_number": current_number,
                        "number_of_thousands": number_of_thousands,
                    }
                )
            number_of_thousands += 1
            num //= 1000
        return thousands[::-1]

    def number_below_thousand(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.Words[num]
        elif num < 100:
            tens = num // 10 * 10
            rest = num % 10
            return self.Words[tens] + ("" if rest == 0 else " " + self.Words[rest])
        else:
            hundreds = num // 100
            rest = num % 100
            return (
                self.Words[hundreds]
                + " Hundred"
                + ("" if rest == 0 else " " + self.number_below_thousand(rest))
            )

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return self.Words[0]

        thousands = self.number_to_thousands(num)
        word_string = ""

        for thousand in thousands:
            current_thousand = thousand["current_number"]
            number_of_thousands = thousand["number_of_thousands"]

            if number_of_thousands == 0:
                word_string += self.number_below_thousand(current_thousand)
            else:
                word_string += (
                    self.number_below_thousand(current_thousand)
                    + " "
                    + self.Words[1000**number_of_thousands]
                    + " "
                )

        return word_string.strip()
