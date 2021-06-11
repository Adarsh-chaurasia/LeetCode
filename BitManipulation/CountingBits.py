def countbits(n):
    count=0
    while n:
        if n&1==1:
            count+=1
        n=n>>1
        
    return count


class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]
        for i in range(0,n+1):
            x=countbits(i)
            output.append(x)
            
            
        return output
            
