class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printAllLevels(root):
   

    queue = [root]
    level = 1

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            current = queue.pop(0)

         
            print(current.val, end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()

  

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)
printAllLevels(root)
