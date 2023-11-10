class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def are_identical_trees(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    
    return (
        tree1.value == tree2.value and
        are_identical_trees(tree1.left , tree2.left)  and
        are_identical_trees(tree1.right, tree2.right)
    )


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(6)
tree2.left.left = TreeNode(4)

if are_identical_trees(tree1, tree2):
    print("The Trees are Identical")
else:
    print("The Trees are not Identical")


