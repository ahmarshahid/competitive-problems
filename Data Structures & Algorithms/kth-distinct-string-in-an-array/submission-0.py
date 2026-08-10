class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        wordSet = set(arr)
        res = []
        for word in arr:
            if arr.count(word)==1:
                k=k-1
                if k==0:
                    return word
        return ""
        
