# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        
        
        if l1.val<l2.val:
            startM=l1
            l1=l1.next
        else:
            startM=l2
            l2=l2.next
        pM=startM
        
        while l1 and l2:
            if l1.val < l2.val :
                pM.next=l1
                pM=pM.next
                l1=l1.next
                
            else:
                pM.next=l2
                pM=pM.next
                l2=l2.next
        if l1:
            pM.next=l1
            
        else:
            pM.next=l2
            
            
            
            
            
            
            
            
            
            
            
            
    
            
            
        return  startM
        
