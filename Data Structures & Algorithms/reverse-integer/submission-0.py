class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x= abs(x)
        rev = 0

        while x>0:
            rev = (rev * 10)+ (x % 10)
            x //= 10
            
        rev = rev*sign
        MIN_INT = -2147483648
        MAX_INT = 2147483647

        if rev<MIN_INT or rev>MAX_INT:
            return 0

        return rev
        