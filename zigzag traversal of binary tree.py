def zigzagLevelOrder(self, A):

        res = []

        q = []
        q.append(A)
        idx = 0

        while q:

            l = len(q)
            lst = deque()

            for i in range(l):
                node = q.pop(0)
                if idx%2!=0:
                    lst.appendleft(node.val)
                else:
                    lst.append(node.val)

                if node.left:
                        q.append(node.left)
                if node.right:
                        q.append(node.right)
            
            idx+=1

            res.append(lst)
            
        return res 
