class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def pathToLeaf(node,path,sums,lo,hi):
    
    if not node:
        return 
    
    if not node.left and not node.right:
        sums+=node.data
        if sums>=lo and sums<=hi:
            print(path+[node.data])
            
        return 
    
    pathToLeaf(node.left,path+[node.data],sums,lo,hi)
    pathToLeaf(node.right,path+[node.data],sums,lo,hi)
    
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
pathToLeaf(root,[],0,2,30)


    
