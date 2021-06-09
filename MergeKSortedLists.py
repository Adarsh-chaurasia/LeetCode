import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minheap=[]
        for i in range(len(lists)):
            head=temp=lists[i]
            while head:
                temp=head.next
                head.next=None
                heapq.heappush(minheap,head.val)
                head=temp
                
        head=tail=None
        while minheap:
            data=heapq.heappop(minheap)
            node=ListNode(data)
            if head==None:
                head=node
                tail=head
            else:
                tail.next=node
                tail=tail.next
        return head
        
