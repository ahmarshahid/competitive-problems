class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]
        for i in nums[1:]:
            currSum = max(i, i+currSum)
            maxSum = max(maxSum, currSum)
        return maxSum