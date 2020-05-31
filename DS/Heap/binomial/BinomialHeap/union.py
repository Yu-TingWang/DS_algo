from DS.Heap.binomial import BinomialNode as Node
from DS.Heap.binomial import BinomialHeap as Heap
from DS.Heap.binomial.BinomialHeap import merge


def union(h1: Heap, h2: Heap) -> Heap:
    """ This takes O(log n) time.
    Creates and returns a new heap that contains all nodes of heaps h1,h2 by :
    repeatedly merges trees whose roots have the same degree.
    :param h1: Binomial Heap
    :param h2: Binomial Heap
    :return: the united binomial heap
    """
    h = Heap()
    h.head = merge(h1, h2)
    # now h is a merged heap of h1 and h2 in order of the degree.
    # there might more than one tree of same degree, so we have to iterate the root list
    # and make some necessary linking i.e. merge two trees of level k to one tree of level k+1
    if not h.head:
        return h
    prev, x = None, h.head
    nex = x.next
    while nex:
        # case 1: x < nex -> heap property is maintained , no need to adjust!
        # case 2: x is the first tree of equal degrees. i.e. x.degree == nex.degree == nex.next.degree
        if x.degree != nex.degree or (nex.next and nex.next.degree == x.degree):
            prev, x = x, nex  # update the pointer one node forward
        # case 3&4 : x is the first of two trees of equal degree.
        # i.e. x.degree = nex.degree != nex.next.degree
        # case 3: x has a smaller key, so x will be the root after linking
        elif x.key <= nex.key:
            x.next = nex.next  # remove nex from the root list
            x.link(nex)  # makes nex the left-most child of x
        # case 4: nex has a smaller key, so nex will be the root after linking
        else:
            # remove x from the root list
            if not prev:
                h.head = nex
            else:
                prev.next = nex
            nex.link(x)  # makes x the left-most child of nex
            # move x one forward
            x = nex
        nex = x.next
    return h