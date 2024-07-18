class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = s.split()
        return " ".join(t[::-1])
