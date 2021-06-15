from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        bfs=[]
        if not root:
            return 0
        
        queue=deque([])
        
        queue.append(root)
        while queue:
            level=len(queue)
            sum_=0
            for i in range(level):
                current=queue.popleft()
                sum_=sum_+current.val
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                    
            bfs.append(sum_)
            
        x=bfs.index(max(bfs))
        
        return x+1
