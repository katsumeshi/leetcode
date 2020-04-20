class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        numbers = []
        alphas = []
        for c in s:
            if c.isalpha():
                alphas.append(c)
            else:
                numbers.append(c)
                
        if abs(len(numbers) - len(alphas)) >= 2:
            return ""
        
        all = numbers+alphas[::-1] if len(numbers) > len(alphas) else alphas+numbers[::-1]
        ans = ""
        while len(all):
            ans += all.pop(0)
            ans += all.pop() if len(all) > 0 else "" 
        return ans 
            
