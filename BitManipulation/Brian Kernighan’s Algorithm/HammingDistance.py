def checkBits(bits):
    count=0
    while bits:
        bits=bits&(bits-1)
        count+=1
        
    return count

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bits=x^y
        
        result=checkBits(bits)
        
        return result
