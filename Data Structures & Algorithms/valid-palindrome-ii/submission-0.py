class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        if s==s[::-1]:
            return True
        while l<r:
            if s[l]!=s[r]:
                sL= s[l+1:r+1]
                sR= s[l:r]
                return sL==sL[::-1] or sR==sR[::-1]
            l,r=l+1,r-1
        return True
        