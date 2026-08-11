class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        detectZero = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                detectZero.append(nums[i])
                del nums[i] 
        if len(detectZero) != 0:
            for j in detectZero:
                nums.append(detectZero[j])
        