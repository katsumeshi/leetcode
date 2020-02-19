class Solution(object):
    def findContentChildren(self, greeds, cookies):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        greeds = sorted(greeds)
        cookies = sorted(cookies)
        i=0
        count = 0
        for greed in greeds:
            if len(cookies) > i:
                cookie=cookies[i]
                last=i
                while len(cookies) > i and cookie < greed:
                    cookie = cookies[i]
                    i += 1
                if cookie >= greed:
                    count += 1
                    if last == i:
                        i += 1
                    
        return count
