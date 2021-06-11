class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i=0
        while True:
            x=4**i
            if x==n:
                return True
            elif x>n:
                break
            i+=1
