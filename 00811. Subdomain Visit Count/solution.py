class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}
        for cpdomain in cpdomains:
            cdomain = cpdomain.split(" ")
            count = int(cdomain[0])
            domain = cdomain[1].split(".")
            for i in range(len(domain)):
                key = ".".join(domain[i:])
                dict[key] = dict[key] + count if key in dict else count
                
        for key in dict:
            dict[key] = str(dict[key]) + " " + key
            
        return dict.values()
