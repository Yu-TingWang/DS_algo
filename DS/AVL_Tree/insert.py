from DS.AVL_Tree import AVL_Node as Node
from DS.AVL_Tree import binary_search


def get_height(n: Node):
    if not n:
        return 0
    return n.height


def insert(root: Node, val: int):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    # update height
    root.height = max(get_height(root.left, root.right)) + 1
    # get the balance factor
    balance = root.get_bf()
    # perform rotation if unbalanced
    if balance > 1:
        # left-right case
        if val > root.left.val:
            root.left = left_rotate(root.left)
        # left case ( both left-left and left-right)
        return right_rotate(root)
    if balance < -1:
        # right-left case
        if val < root.right.val:
            root.right = right_rotate(root.right)
        # right case ( both right-left and right-right)
        return left_rotate(root)
    return root


def right_rotate(root: Node) -> Node:
    new_root = root.left
    temp_right = new_root.right
    new_root.right = root  # move up the new root and makes old root its right child
    root.left = temp_right  # move the right child of new root to be old_root.right.left
    return new_root


def left_rotate(root: Node) -> Node:
    new_root = root.right
    temp_left = new_root.left
    new_root.left = root
    root.right = temp_left
    return new_root
