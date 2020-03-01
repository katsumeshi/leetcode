class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        consonant = "maa"
        sentences = S.split(" ")
        
        for i in range(len(sentences)):
            if sentences[i][0] in vowels:
                sentences[i] += consonant
            else:
                sentences[i] = sentences[i][1:] + sentences[i][0] + consonant
            consonant += "a"
                    
        return " ".join(sentences)
