class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = sorted(nums)
        n = len(num)
        return num[n-k]
        