class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {
                    'I':1,
                    'IV':4,
                    'V':5,
                    'IX':9,
                    'X':10,
                    'XL':40,
                    'L':50,
                    'XC':90,
                    'C':100,
                    'CD':400,
                    'D':500,
                    'CM':900,
                    'M':1000
                }
        sum = 0
        new_roman = []
        i=0
        while i<len(s):
            if i+1<len(s) and s[i] + s[i+1] in roman_to_int:
                new_roman.append(s[i] + s[i + 1])
                i+=2
            else:
                new_roman.append(s[i])
                i+=1
            
        for l in new_roman:
            sum += roman_to_int[l]
        return sum
