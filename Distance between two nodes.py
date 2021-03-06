class Node:
    def __init__(self,data):
        self.data = data 
        self.right = None
        self.left = None 
        
def findPath(root,path,k):
    if not root:
        return 
    
    path.append(root.data)
    
    if root.data==k:
        return True 
        
    if root.left!=None and findPath(root.left,path,k) or root.right!=None and findPath(root.right,path,k):
        return True 
        
    path.pop()
    return False 
    
def findLCA(root,n1,n2):
    
    path1 = []
    path2 = []
    
    if not findPath(root,path1,n1) or not findPath(root,path2,n2):
        return -1 
        
    i = 0

    while i<len(path1) and i<len(path2):
        
        if path1[i] != path2[i]:
            break 
        
        i+=1 
        
    return len(path1)+len(path2) - 2*i
    
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
