from DS.Heap.binomial import BinomialNode as Node
from DS.Heap.binomial import BinomialHeap as Heap
from DS.Heap.binomial.BinomialHeap import _min


def get_min(h: Heap) -> Node:
    """
    Find the node whose key is minimum among the heap. Takes O(log n ) time.
    :param h: Binomial Heap
    :return: The node with minimum key in the Binomial Heap.
    """
    prev, curr = _min(h)
    return curr
