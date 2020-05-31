from DS.Heap.binomial import BinomialNode as Node
from DS.Heap.binomial import BinomialHeap as Heap
from DS.Heap.binomial.BinomialHeap import union, _min, _reverse


def extract_min(h: Heap) -> Node:
    """
    First, iterate the root list to get the minimum key.
    Second, for the tree whose roots being extracted, promote its children.
    Third, adjust the tree. ( merging trees of equal degree. )
    :param h:
    :return:
    """
    # find the root with min key in root list, and remove it
    prev, min_node = _min(h)
    # remove the list from root list
    if not prev:
        h.head = min_node.next
    else:
        prev.next = min_node.next
    # reverse the order of its children and
    reverse = _reverse(min_node)
    rev = Heap(reverse)
    h = union(h, rev)
    # cut the reference
    min_node.next = min_node.child = None
    min_node.degree = 0
    return min_node
