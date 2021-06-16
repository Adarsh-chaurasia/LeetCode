def inOrder(root):
    output=[]
    stack=[]
    current=root
    
    while True:
        if current:
           stack.append(current)
           current=current.left
           
        elif stack:
            current=stack.pop()
            output.append(current.data)
            
            
            
            current=current.right
            
        else:
            break
        
        
    return output
