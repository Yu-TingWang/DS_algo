class AVL_Node():
    def __init__(self,x=None):
        self.val=x
        self.bf=0 # the balance factor
        self.height=0
        self.right=None
        self.left=None

    def set_left(self,x):
        self.left = AVL_Node(x)
        self.height+=1



