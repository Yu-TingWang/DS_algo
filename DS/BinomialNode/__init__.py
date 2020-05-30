"""
Each binomial tree follows a min-heap property:
1.The key of each node is greater than or equal to the key of its parent.
2.Stored in the left-child, right-sibling representation
  The child pointer points to the left-most child node, and each child has a next pointer pointing to its
  right sibling. The right-most sibling points to null.
  For heap: If x is a root, then x.next points to the next root in the root list.
3. degree represents the number of children the node has ** not grandchildren, only considering direct children.
"""
from DS import BinomialNode as Node


class BinomialNode:

    def __init__(self, key: int, value=None):
        self.key = key
        self.value = value
        self.degree = 0  # default degree
        self.parent = self.next = self.child = None

    def setValue(self, value):
        self.value = value

    def decrease(self, new_key: int):
        """
        Assign new_key to self.key and bubble up if necessary.
        :param new_key:
        :return:
        """
        assert new_key < self.key, f"key must be smaller than the original key. Original: {self.key}, Got: {new_key}"
        node = self
        node.key = new_key
        curr = node
        parent = curr.parent
        # bubble up
        while parent and curr.key < parent.key:
            # swap the attribute
            parent.key, curr.key = curr.key, parent.key
            parent.value, curr.value = curr.value, parent.value
            # update pointer up
            curr = parent
            parent = curr.parent

    def link(self, sub: Node):
        """
        Merge sub into self as its left-most child
        :param sub:
        :return:
        """
        sub.parent = self  # set self as sub's parent
        sub.next = self.child  # set the original left-most child as next node to sub
        self.child = sub  # cut the original self child pointer, and reconnect to sub
        # update degree
        self.degree += 1


"""
For Binomial Tree B_k,
1. there are 2^k nodes
2. height of tree is k
3. there are exactly C(k,i) nodes at depth i for i in [0,k]
4. the root has degree k, which is greater than that of any other node;
   if the children of the root are numbered from left to right [k-1, ... ,0]
   then child i is the root of subtree B_i. 
5. the max degree of any node in n-node binomial tree is log(n)
"""
