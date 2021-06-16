from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        bfs=deque([])
        if not root:
            return []
        
        queue=deque([])
        
        queue.append(root)
        while queue:
            level=len(queue)
            curr=[]
            for i in range(level):
                current=queue.popleft()
                curr.append(current.val)
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                    
            bfs.appendleft(curr)
            
        
        
        return bfs

        
        
        
        
 #AnotherApproach

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        bfs=[]
        if not root:
            return []
        
        queue=deque([])
        
        queue.append(root)
        while queue:
            level=len(queue)
            curr=[]
            for i in range(level):
                current=queue.popleft()
                curr.append(current.val)
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                    
            bfs.append(curr)
            
        output=list(reversed(bfs))
        
        return output

        
