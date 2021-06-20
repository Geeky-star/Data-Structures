
class newNode:
    
    def __init__(self,val):
        self.data = val 
        self.right=None 
        self.left = None 
  
   
def bfs(node):
    
    s1 = []
    s2 = []
    s1.append(node) 
    while len(s1)!=0 or len(s2)!=0:
        
        while len(s1)!=0:
            node = s1.pop()
            print(node.data,end=" ")
            if node.right:
                s2.append(node.right)
            if node.left:
                s2.append(node.left)
                
        while len(s2)!=0:
            node = s2.pop()
            print(node.data,end=" ")
            if node.left:
                s1.append(node.left)
                
            if node.right:
                s1.append(node.right)
                
                
if __name__ == '__main__':
    root = newNode(1) 
    root.left = newNode(2) 
    root.right = newNode(3) 
    root.left.left = newNode(7) 
    root.left.right = newNode(6) 
    root.right.left = newNode(5) 
    root.right.right = newNode(4) 
    print("Spiral Order traversal of",
                    "binary tree is ") 
    bfs(root)
    
