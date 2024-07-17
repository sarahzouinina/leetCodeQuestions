class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_in_string = []
        j = 0
        output = ""

        for i in range(len(s)):
            if s[i] in vowels:
                vowels_in_string.append(s[i])
        vowels_in_string = vowels_in_string[::-1]
       
        for i in range(len(s)):
            if s[i] in vowels:
                output += vowels_in_string[j]
                j += 1
            else:
                output += s[i]
        return output
