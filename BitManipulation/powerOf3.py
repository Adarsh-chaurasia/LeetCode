class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i=0
        while True:
            x=3**i
            if x==n:
                return True
            elif x>n:
                break
            i+=1
