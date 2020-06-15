from DS.BinaryNode import BinaryNode as Node


class AVL_Node(Node):
    def __init__(self, x=None):
        super().__init__(x)

    def get_bf(self):
        # the balance factor is defined as the difference between the height of its right child and left child
        # for an AVL node, it has to be -1,0,1
        if self.right and not self.left:
            bf = self.right.height
        elif self.left and not self.right:
            bf = - self.left.height
        elif not self.right and not self.left:
            bf = 0
        else:
            bf = self.right.height - self.left.height
        return bf
