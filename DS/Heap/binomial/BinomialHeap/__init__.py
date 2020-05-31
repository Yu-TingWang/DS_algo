from DS.Heap.binomial import BinomialNode as Node
from DS.Heap.binomial import BinomialHeap as Heap



class BinomialHeap:
    """
    BinomialHeap is organized as a linkedlist, -> root list
    where each node is the root of a binomial tree in order of strictly increasing degree.
    """

    def __init__(self, h: Node = None):
        self.head = h


