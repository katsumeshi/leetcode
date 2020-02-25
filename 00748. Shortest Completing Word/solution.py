class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        r = re.findall('[a-zA-Z]', licensePlate)
        words = sorted(words, key=len)
        w = copy.deepcopy()
        for c in r:
            for i in range(len(w)):
                if w[i] is None:
                    continue
                try:
                    c = c.lower()
                    index = w[i].index(c)
                    w[i] = w[i][:index] + w[i][index+1:]
                except ValueError:
                    w[i] = None
        for i in range(len(w)):
            if w[i] is not None:
                return words[i]
