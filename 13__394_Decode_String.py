import re
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        pattern = re.compile(r'(\d+)\[([a-zA-Z]*)\]')

        def replace_match(match):
            count = int(match.group(1)) 
            string = match.group(2) 
            return count * string 

        while '[' in s:
            s = pattern.sub(replace_match, s)
        return s
