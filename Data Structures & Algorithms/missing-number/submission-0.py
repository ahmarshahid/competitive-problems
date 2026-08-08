class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        numSet = set(nums)
        numbers = list(numSet)
        for i in range(len(numbers)):
            if numbers[i] != i:
                return i
        return len(numbers)
        