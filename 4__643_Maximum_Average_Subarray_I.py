class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])
        max_avg = window_sum
        n =len(nums)

        # Slide the window from start to end in the array
        for i in range(n-k):
            window_sum = window_sum - nums[i] + nums[i+k]
            max_avg = max(max_avg, window_sum)
        return max_avg /float(k)
