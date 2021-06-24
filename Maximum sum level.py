from collections import deque

class Node:
    
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 
        
        
def bfs(root):

    q = deque()
    q.append(root)
    
    ans = root.data 
    while len(q)>0:
        sums = 0
        
        n = len(q)
        while n>0:
            node=q.popleft()
            sums+=node.data
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
            n-=1 
            
        ans = max(ans,sums)
        
    return ans
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

print(bfs(root))
