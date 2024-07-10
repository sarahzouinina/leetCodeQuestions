class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        cpt = 0
        for log in logs:
            if log == "./":
                cpt += 0
            elif (log == "../"):
                if cpt>0:
                    cpt -= 1
            else: cpt += 1
        return cpt
# 32ms runtime and 11.8 MB  Memory
  
