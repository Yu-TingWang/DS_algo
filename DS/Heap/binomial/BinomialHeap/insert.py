from DS.Heap.binomial import BinomialNode as Node
from DS.Heap.binomial import BinomialHeap as Heap
from DS.Heap.binomial.BinomialHeap import union


def insert(h: Heap, k: int):
    """
    Insert a node with key k to binomial heap h
    :param h: BinomialHeap, where k to be inserted
    :param k: int, key value
    :return:
    """
    node = Node(k)
    h1 = Heap(node)
    h = union(h, h1)