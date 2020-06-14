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

# Method 2: Use a BST-tree
"""
In this approach, we traverse the input array from the ending to the begging and add the elements into the BST.
While inserting the elements to the BST, we can compute the number of elements which are lesser elements simply 
by computing the sum of frequency of the element and the number of elements to the left side of current node,
if we are moving to right side of the current node.
Once we place an element in it’s correct position, we can return this sum value.
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None
        # augmented attribute
        self.frequency = 1  # the number of times an element has occurred
        self.left_count = 0  # the number of left elements we have encountered


class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, node: Node):
        """
        Place an element (A[i]) at its correct position in the BST and return the corresponding element of B[i]
        :param node:
        :return:
        """
        curr = self.root
        result=0
        while curr:
            prev=curr
            if node.val>curr.val:
                # compute the number of elements that are less than the current node
                result += curr.frequency + curr.left_count
                curr = curr.right
            elif node.val < curr.val:
                curr.left_count +=1
                curr = curr.left
            else:
                prev = curr
                prev.frequency +=1
                break
        if prev.val>node.val:
            prev.left=node
        elif prev.val<node.val:
            prev.right=node
        else:
            return result + prev.left_count
        return result


def construct_B(A:list):
    t = Tree(Node(A[-1])) # start from the end of the array
    B=[0]
    for i in range(len(A)-2,-1,-1):
        B.append(t.insert(Node(A[i])))
    return B[::-1]


if __name__ == "__main__":
    A = [3, 5, 1, 4, 7, 6, 2]
    print(construct_B(A))