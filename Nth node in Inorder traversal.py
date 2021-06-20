class Node:
    
    def __init__(self,val):
        self.data = val 
        self.right=None 
        self.left = None 
  
   

def NthInorder(node,n,count):
    
    if not node:
        return 
        
    if count<=n:
         NthInorder(node.left,n,count)
         count = count+1
         if count==n:
            print("Node is - ",node.data,count)
        
         NthInorder(node.right,n,count)
    
root = Node(10) 
root.left = Node(20) 
root.right = Node(30) 
root.left.left = Node(40) 
root.left.right = Node(50) 
  
n = 4
NthInorder(root, n,count = 0)
