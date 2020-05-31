from DS.Heap.binomial import BinomialNode as Node
from DS.Heap.binomial import BinomialHeap as Heap


def _reverse(h: Heap) -> Heap.head:
    """
    Private method. Takes O(log n).
    Aside: n = # nodes, then # trees = log(n),
    Given a root of binomial heap, return a new heap with its children and reverse their children to maintain
    the heap property.
    :param h: the root of the binomial heap
    :return: the head pointer ot the heap
    """
    if not h: return None
    tail, curr = None, h.head
    curr.parent = None
    while curr.next:
        # reverse
        head = curr.next
        curr.next = tail
        # update the pointer
        tail = curr
        curr = head
        curr.parent = None
    curr.next = tail
    return curr
