class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        queue = deque([root])
        while queue:
            l = len(queue)
            r = []
            for i in range(l):
                node = queue.popleft()
                r.append(node.val)
                for j in range(len(node.children)):
                    queue.append(node.children[j])
            
            if len(r)!=0:   
                ans.append(r)
            
        return ans
