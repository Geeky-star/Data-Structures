def height(root):
    
    if not root:
        return 0
        
    return max(height(root.left),height(root.right))+1

def isBalanced(root):
    if root is None:
        return True
    
    ldepth = height(root.left)
    rdepth = height(root.right)
    
    
    if max(ldepth-rdepth,rdepth-ldepth)<=1 and isBalanced(root.left) and isBalanced(root.right):
        return 1
        
    else:
        return 0
