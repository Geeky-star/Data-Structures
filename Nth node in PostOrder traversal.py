class Node:
    
    def __init__(self,val):
        self.data = val 
        self.right=None 
        self.left = None 
  
   
count = [0]
def NthInorder(node,n,count):
    
    if not node:
        return 
        
    if count[0]<=n:
         NthInorder(node.left,n,count)
         NthInorder(node.right,n,count)
         count[0] = count[0]+1
         if count[0]==n:
            print("Node is - ",node.data)
    
root = Node(10) 
root.left = Node(20) 
root.right = Node(30) 
root.left.left = Node(40) 
root.left.right = Node(50) 
  
n = 4
NthInorder(root, n,count)
