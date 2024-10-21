# https://leetcode.com/problems/bulls-and-cows/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM%2CHARD
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        char_freq = Counter(secret)

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                if char_freq[secret[i]] == 0:
                    cows -= 1
                    char_freq[secret[i]] = 1
                char_freq[secret[i]] -= 1
                bulls += 1
            elif guess[i] in char_freq and char_freq[guess[i]] > 0:
                cows += 1
                char_freq[guess[i]] -= 1

        return str(bulls) + "A" + str(cows) + "B"
