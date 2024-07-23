class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums)-1
        cpt = 0
        sum_sub = 0
        while left<right:
            sum_sub = nums[left] + nums[right]
            if sum_sub == k:
                cpt +=1
                left +=1
                right -=1
            elif sum_sub<k:
                left +=1
            else: 
                right -=1
        return cpt
