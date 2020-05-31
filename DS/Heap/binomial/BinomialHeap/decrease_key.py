from DS.Heap.binomial import BinomialNode as Node
from DS.Heap.binomial import BinomialHeap as Heap


def decrease_key(h: Heap, x: Node, k: int):
    """
    Decrease the key value of x, and the new key value has to be no greater than the original one.
    :param h: a Binomial Heap
    :param x: a Binomial Node in heap
    :param k: a new key that is to be assigned to x.
    :return:
    """
    assert k < x.key, f"key must be smaller than the original key. Original: {k}, Got: {x.key}"
    x.decrease(k)