class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d={}
        
        for each in stones:
            if each in d:
                d[each]+=1
            else:
                d[each]=1
                
        result=0
        for char in jewels:
            if char in d:
                result+=d[char]
            else:
                result+=0
                
        return result
