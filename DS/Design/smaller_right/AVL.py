"""
You are given an input array A of n distinct numbers, and you want to compute an output array B, in
which B[i] is the number of such elements in A: (a) the element appears after A[i] in A, and (b) the
element is strictly smaller than A[i].
For example, if the input is A = [3; 5; 1; 4; 7; 6; 2], then the output should be B = [2; 3; 0; 1; 2; 1; 0]. Because
in A, after 3 (i.e., A[1]) there are 2 elements that are smaller than 3 (i.e., 1 and 2); and after 5 (i.e., A[2])
there are 3 elements that are smaller than 5 (i.e., 1, 4 and 2), etc.
Now you need to design an algorithm that computes B using A. The runtime of your algorithm must be
O(n log n) in worst case, where n is the size of A.
"""

# Method 1: Use an AVL-Tree
"""
In this approach, we use a self-balanced bst, (doesn't have to be AVL, could be red-black)
we traverse the input array from the ending to the begging and add the elements into the AVL.
When inserting A[i], we compare it with the root.  If it is greater than the root, then it is greater
than all nodes in the left-subtree. Hence the size of the left sub-tree is B[i] for A[i]. 
"""


class Node():
    """
    We augment the AVL such that every node N contains size the subtree rooted at N.
    """

    def __init__(self, x):
        self.left = self.right = None
        self.key = x
        self.height = 1
        self.size = 1


def get_size(n: Node):
    if not n:
        return 0
    return n.size


def get_height(n: Node):
    if not n:
        return 0
    return n.height


def right_rotate(n: Node):
    new_root = n.left
    old_right = new_root.right
    # rotate
    n.left = old_right
    new_root.right = n
    # update height
    n.height = max(get_height(n.left), get_height(n.right)) + 1
    new_root.height = max(get_height(new_root.right), get_height(new_root.left)) + 1
    # update size
    n.size = get_size(n.left) + get_size(n.right) + 1
    new_root.size = get_size(new_root.left) + get_size(new_root.right) + 1
    return new_root


def left_rotate(n: Node):
    new_root = n.right
    old_left = new_root.left
    # rotate
    n.right = old_left
    new_root.left = n
    # update height
    n.height = max(get_height(n.left), get_height(n.right)) + 1
    new_root.height = max(get_height(new_root.right), get_height(new_root.left)) + 1
    # update size
    n.size = get_size(n.left) + get_size(n.right) + 1
    new_root.size = get_size(new_root.left) + get_size(new_root.right) + 1
    return new_root


def get_balance(n: Node):
    return get_height(n.left) - get_height(n.right)


def insert(root: Node, key: int, index: int, count: list):
    """
    Insert a node with key in root, and update count[index] while inserting.
    :param root: root of the avl tree
    :param key: A[i]
    :param index: the index of current node on the input array
    :param count: B, the output list to be modified
    :return: the root of the tree after insertion
    """
    # perform insertion
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key, index, count)
    else:
        root.right = insert(root.right, key, index, count)
        count[index] += get_size(root.left) + 1
    # update height and size
    root.height = max(get_height(root.left), get_height(root.right)) + 1
    root.size = max(get_size(root.left), get_size(root.right)) + 1
    # get the balance factor
    balance = get_balance(root)
    # perform rotation if unbalanced
    # left-left case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    # right-right case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    # left-right case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # right-left case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root


def construct(A: list):
    t = Node(A[-1])  # start from the end of the array
    root = Node(A[-1])
    B=[0]*len(A)
    for i in range(len(A) - 2, -1, -1):
        root = insert(root, A[i], i, B)
    return B


if __name__ == "__main__":
    A = [3, 5, 1, 4, 7, 6, 2]
    print(construct(A))
