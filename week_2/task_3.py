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
        number_of_thousands = 0
        thousands = []
        while num > 0:
            current_number = num % 1000
            thousands.append(
                {
                    "current_number": current_number,
                    "number_of_thousands": number_of_thousands,
                }
            )
            number_of_thousands += 1
            num = num // 1000
        return thousands[::-1]

    def thousands_to_tens(self, num):
        tens = []
        number_of_tens = 0
        while num > 0:
            current_number = num % 10
            tens.append(
                {"current_number": current_number, "number_of_tens": number_of_tens}
            )
            num = num // 10
            number_of_tens += 1
        return tens[::-1]

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

            if number_of_thousands > 0:
                if current_thousand < 20:
                    word_string += (
                        " "
                        + self.Words[current_thousand]
                        + " "
                        + self.Words[1000**number_of_thousands]
                    )
                else:
                    tens = self.thousands_to_tens(current_thousand)
                    for ten in tens:
                        current_ten = ten["current_number"]
                        number_of_tens = ten["number_of_tens"]

                        if number_of_tens == 0 or number_of_tens == 1:
                            word_string += (
                                " " + self.Words[current_ten * 10**number_of_tens]
                            )
                        else:
                            word_string += (
                                " "
                                + self.Words[current_ten]
                                + " "
                                + self.Words[10**number_of_tens]
                            )

                    word_string += " " + self.Words[1000**number_of_thousands]
            else:
                # # if current_thousand<=20:
                # #     word_string+=' '+self.Words[current_thousand]
                # # elif (current_thousand%10==0 and current_thousand!=100):
                # #     word_string+=' '+self.Words[current_thousand]
                # else:
                tens = self.thousands_to_tens(current_thousand)
                for ten in tens:
                    current_ten = ten["current_number"]
                    number_of_tens = ten["number_of_tens"]
                    if (
                        number_of_tens == 0
                        or number_of_tens == 1
                        and current_ten * 10**number_of_tens >= 20
                    ):
                        word_string += (
                            " " + self.Words[current_ten * 10**number_of_tens]
                        )
                    else:
                        word_string += (
                            " "
                            + self.Words[current_ten]
                            + " "
                            + self.Words[10**number_of_tens]
                        )

        return word_string.strip()


solution = Solution()
print(solution.numberToWords(1000000))
