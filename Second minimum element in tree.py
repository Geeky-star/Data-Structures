class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
        queue = deque([root])
        res=[]
        res.append(root.val)
        while queue:
            node = queue.pop()
            
            if node.left:
                res.append(node.left.val)
                queue.append(node.left)               
                
            if node.right:
                res.append(node.right.val)
                queue.append(node.right)
    
        s = sorted(set(res))
        return s[1] if len(s)>1 else -1
