from DS.Heap.binomial import BinomialNode as Node
from DS.Heap.binomial import BinomialHeap as Heap


def merge(h1: Heap, h2: Heap):
    """
    Merge two heap roots, sorted by degree, and return new head.
    Note: This function simply merges these two heaps, it does not check if the heap property is maintained.
    i.e.
    :type h1: heap.head
    :param h1:
    :param h2:
    :return: the head of merged heap in order of increasing degree; trees of same degree are adjacent.
    """
    if not h1.head:
        return h2
    if not h2.head:
        return h1
    if h1.head.degree < h2.head.degree:
        h = h1.head
        h1 = h.next
    else:
        h = h2.head
        h2 = h.next
    prev = h
    # Initially, there are at most two roots on h of the same degree. Since there are two heaps.
    # This loop will makes the tree whose roots of same degree to be adjacent in the root list. (h)
    while h2 and h1:
        if h1.degree < h2.degree:
            prev.next = h1
            h1 = h1.next
        else:
            prev.next = h2
            h2 = h2.next
        prev = prev.next
    if h2:
        prev.next = h2
    else:
        prev.next = h1
    return h
