def solve(arr,k,i):
    if len(arr)==1:
        return arr[0]
        
    i=(i+k)%len(arr)
    
    arr.pop(i)
    
    return solve(arr,k,i)


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
            
        s=k-1
        
        res=solve(arr,s,0)
        return res
