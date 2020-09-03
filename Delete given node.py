class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root):

    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def insert(root,data):
    if root is None:
        return Node(data)

    if data<root.data:
        root.left = insert(root.left,data)

    else:
        root.right = insert(root.right,data)

    return root


def minValue(node):

    current=node

    while current.left is not None:
        current=current.left

    return current

def deleteNode(root,data):

    if root is None:
        return root

    if data<root.data:
        root.left = deleteNode(root.left,data)

    elif data>root.data:
        root.right = deleteNode(root.right,data)

    else:

        if root.left is None:
            temp=root.right
            root=None
            return temp

        elif root.right is None:
            temp=root.left
            root=None
            return temp

        temp = minValue(root.right)
        root.data = temp.data

        root.right = deleteNode(root.right,temp.data)

    return root

root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,60)
root = insert(root,80)

print("Inorder traversal of tree: ")
inorder(root)

print("\n Delete 20")
root = deleteNode(root,20)
print("\nInorder traversal after deleting 20: ")
inorder(root)

print("\n Delete 50")
root = deleteNode(root,50)
print("\nInorder traversal after deleting 50: ")
inorder(root)
