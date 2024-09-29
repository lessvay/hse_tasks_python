class WordDictionary(object):

    def __init__(self):
        self.items = []

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.items.append(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        for item in self.items:
            if len(item) == len(word):
                match = True
                for i in range(len(word)):
                    if word[i] != "." and word[i] != item[i]:
                        match = False
                        break
                if match:
                    return True
        return False
