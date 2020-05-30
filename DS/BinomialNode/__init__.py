from DS import BinomialNode as Node

class BinomialNode():
    def __init__(self,key:int):
        self.key=key
        self.degree=0 # default degree
        self.parent = self.sibiling = None
        self.child=[]

    def setParent(self,parent:Node):
        self.parent = parent

    def setDegree(self,degree:int):
        self.degree = degree

    def setSibiling(self,sibiling:Node):
        # points to right sibiling
        # the right-most's sibiling points to null
        self.sibiling = sibiling

    def addChild(self,child:Node):
        self.child.append(child)