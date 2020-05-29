class BinomialNode():
    def __init__(self):
        self.parent=None
        self.key=None
        self.degree=None
        self.child=None
        self.sibiling=None

    def setKey(self,key:int):
        self.key=key

    def setParent(self,parent):
        self.parent = parent

    def setDegree(self,degree:int):
        self.degree = degree

    def setSibiling(self,sibiling):
        self.sibiling = sibiling