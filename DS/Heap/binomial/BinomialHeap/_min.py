from DS.Heap.binomial import BinomialNode as Node
from DS.Heap.binomial import BinomialHeap as Heap


def _min(h: Heap) -> (Node, Node):
    """
    Private method. Takes O(log n)
    Return the previous node of min_node and min_node.
    :param h:
    :return:
    """
    import math
    curr_min = math.inf
    prev = None
    x = h.head
    # iterate the root list
    while x:
        if x.key < curr_min:  # update curr_min
            curr_min = x.key
            prev = x
        x = x.next
    return prev, x
