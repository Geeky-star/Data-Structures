class Node: 
  
    def __init__(self, key): 
        self.key = key 
        self.left = None 
        self.right = None 

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def isComplete(root,index,numberOfNodes):
    if root is None:
        return True
    
    if index>=numberOfNodes:
        return False

    return isComplete(root.left,2*index+1,numberOfNodes) and isComplete(root.right,2*index+2,numberOfNodes)



root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(6) 
  
node_count = count_nodes(root) 
index = 0 
  
if isComplete(root, index, node_count): 
    print("The Binary Tree is complete")
else: 
    print("The Binary Tree is not complete")



    
