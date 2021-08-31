class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap=dict()
        
        for i in arr:
            if i in hashmap:
                hashmap[i]+=1
                
            else:
                hashmap[i]=1
                
        list1=[]
        
        for k,v in hashmap.items():
            if k==v:
                list1.append(k)
            
                
        if list1:
            return max(list1)
        else:
            return -1
