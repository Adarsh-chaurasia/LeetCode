class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        result=n//2
        
        
        unique=set(candyType)
        
        if result==len(unique):
            return result
        elif result<len(unique):
            return result
        
        else:
            return len(unique)
        
        
        
