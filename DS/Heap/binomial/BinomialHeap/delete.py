from DS.Heap.binomial import BinomialNode as Node
from DS.Heap.binomial import BinomialHeap as Heap
from DS.Heap.binomial.BinomialHeap.extract_min import extract_min


def delete(h: Heap, x: Node):
    """
    Delete node x from heap h.
    :param h: a Binomial Heap
    :param x: a Binomial BinaryNode in heap
    :return:
    """
    import math
    # decrease x to the last node
    x.decrease(-math.inf)
    # and then extract min
    extract_min(h)