from collections import deque 

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def diagonalPrint(root,m,d):
    if not root:
        return 
    
    try:
        m[d].append(root.data)
    except:
        m[d] = [root.data] 
        
    diagonalPrint(root.left,m,d+1)
    diagonalPrint(root.right,m,d)
    
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
 
m = dict()
d = 0
diagonalPrint(root,m,d)
for i in range(len(m)):
    print(m[i],end = " ")
  
