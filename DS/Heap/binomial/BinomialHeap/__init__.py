from DS.Heap.binomial import BinomialNode as Node
from DS.Heap.binomial import BinomialHeap as Heap
import math


class BinomialHeap:
    """
    BinomialHeap is organized as a linkedlist, -> root list
    where each node is the root of a binomial tree in order of strictly increasing degree.
    """

    def __init__(self, h: Node = None):
        self.head = h

    def __init__(self, array: list):
        """
        Given an array of size that is power of two, construct a binomial heap.
        :param array:
        """
        assert math.log(len(array), 2).is_integer(), f"length of array must be power of two. Got: {len(array)}"

