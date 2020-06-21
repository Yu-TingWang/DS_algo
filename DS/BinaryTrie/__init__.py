class BinaryTrie:
    def __init__(self,x):
        self.child=[None,None]
        # self.child[0] is the left child
        # self.child[1] is the right child
        self.jump = self.prev = self.next = None
        self.val = x

