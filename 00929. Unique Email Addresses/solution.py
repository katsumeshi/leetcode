class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        for i in range(len(emails)):
            e = emails[i].split("@")
            emails[i] = re.sub("\+.*|\.", "", e[0]) + "@" + e[1]
        return len(set(emails))
