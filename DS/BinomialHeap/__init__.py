from DS import BinomialNode as Node
from DS import BinomialHeap as Heap


class BinomialHeap:
    """
    BinomialHeap is organized as a linkedlist, -> root list
    where each node is the root of a binomial tree in order of strictly increasing degree.
    """

    def __init__(self, h: Node = None):
        self.head = h


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


def get_min(h: Heap) -> Node:
    """
    Find the node whose key is minimum among the heap. Takes O(log n ) time.
    :param h: Binomial Heap
    :return: The node with minimum key in the Binomial Heap.
    """
    prev, curr = _min(h)
    return curr


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



def union(h1: Heap, h2: Heap) -> Heap:
    """ This takes O(log n) time.
    Creates and returns a new heap that contains all nodes of heaps h1,h2 by :
    repeatedly merges trees whose roots have the same degree.
    :param h1: Binomial Heap
    :param h2: Binomial Heap
    :return: the united binomial heap
    """
    h = BinomialHeap()
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
    if not h1.head: return h2
    if not h2.head: return h1
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


def decrease_key(h: Heap, x: Node, k: int):
    """
    Decrease the key value of x, and the new key value has to be no greater than the original one.
    :param h: a Binomial Heap
    :param x: a Binomial Node in heap
    :param k: a new key that is to be assigned to x.
    :return:
    """
    x.decrease(k)


def delete(h: Heap, x: Node):
    """
    Delete node x from heap h.
    :param h: a Binomial Heap
    :param x: a Binomial Node in heap
    :return:
    """
    import math
    # decrease x to the last node
    x.decrease(-math.inf)
    # and then extract min
    extract_min(h)
