class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copy = nums.copy()
        ans = nums + copy
        return ans