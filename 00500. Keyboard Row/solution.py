class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboards = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        
        def func(word):
            ans = False
            for keyboard in keyboards:
                count = 0
                wordSet = set(word.lower())
                for c in wordSet:
                    if c in keyboard:
                        count += 1
                if count == len(wordSet):
                    ans = True
            return ans

        return filter(func ,words)
