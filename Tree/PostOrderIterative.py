def preOrder(root):
    if not root:
        return 
    stack=[]
    stack.append(root)
    output=[]
    while len(stack):
        node=stack.pop()
        output.append(node.data)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
            
    return output
    
