def findIndex(arr):
    low=0
    high=arr.length()-1
    while(low<=high):
        mid=(low+high)//2
        midElement=arr.get(mid)
        if (mid-1)>=0 and midElement>arr.get(mid-1) and (mid+1)<=arr.length() and midElement>arr.get(mid+1):
            return mid
        elif (mid-1)>= 0 and arr.get(mid-1)>midElement:
            high=mid-1
        else:
            low=mid+1

    return high
    
def searchIncreasing(arr,start,end,target):
    while start<=end:
        mid=(start+end)//2
        midElement=arr.get(mid)
        if midElement==target:
            return mid
        elif midElement>target:
            end=mid-1
        else:
            start=mid+1
            
    return -1

def searchDecreasing(arr,start,end,target):
    while start<=end:
        mid=(start+end)//2
        midElement=arr.get(mid)
        if midElement==target:
            return mid
        elif midElement>target:
            start=mid+1
        else:
            end=mid-1
            
    return -1
            
    

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        index=findIndex(arr)
        left=0
        right=arr.length()-1
        if arr.get(index)==target:
            return index
        ans=searchIncreasing(arr,left,index,target)
        if ans!=-1:
            return ans
        return searchDecreasing(arr,index+1,right,target)
        
        
        
        return result
