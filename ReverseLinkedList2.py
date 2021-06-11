# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
            
        l[m-1:n]=l[m-1:n][::-1]
        
        head=None
        tail=None
        for each in l:
            Node=ListNode(each)
            
            if head==None:
                head=tail=Node
            
            else:
                tail.next=Node
                tail=tail.next
                
        return head
        
