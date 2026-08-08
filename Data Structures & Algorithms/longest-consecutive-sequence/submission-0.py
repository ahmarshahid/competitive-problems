class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = sorted(nums)
        numSet = set(numbers)
        longest=0
        for i in numbers:
            length = 0
            if (i-1) not in numSet:
                while (i+length) in numSet:
                    length +=1
                longest = max(longest,length)
        return longest
        