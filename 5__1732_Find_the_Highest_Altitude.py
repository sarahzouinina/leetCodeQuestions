class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        i=len(gain)
        sum_element=[]
        highest = 0
        while i>0:
            sum_element.append(sum(gain[0:i]))
            i -=1
        highest = max(sum_element)
        return max(highest, 0) 
