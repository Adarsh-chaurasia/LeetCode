class Solution:
    def floorSqrt(self, x): 
        if x==1:
            return x
        low,high=2,x//2
        while low<=high:
            mid=(low+high)//2
            num=mid*mid
            if num<x:
                low=mid+1
            elif num>x:
                high=mid-1
            else:
                return mid
        return high
