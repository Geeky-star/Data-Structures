from collections import deque

class newNode:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
        

def maxLevel(root):
    
    if root is None:
        return 0
        
    q = deque()
    q.append(root)
    level = 0
    maxCount = 1
    while (1):
        l = len(q)
        if l==0:
            break 
        
        if l>maxCount:
            ans = level
            maxCount = l 
            
        for i in range(l):
            node = q.popleft()
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
           
        level+=1
                
    return ans
    

root = newNode(2)     #     2    
root.left     = newNode(1)     #     / \
root.right     = newNode(3)     #     1     3    
root.left.left = newNode(4)     # / \ \
root.left.right = newNode(6)     # 4     6 8
root.right.right = newNode(8) #     /    
root.left.right.left = newNode(5)#

ans =  maxLevel(root)   
print(ans)
        
