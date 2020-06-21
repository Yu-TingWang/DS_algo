from DS.BinaryTrie import BinaryTrie as Trie
def find(x:str, t:Trie):
    """
    Find the predecessor of x in t.
    i.e. max{ y in t| y<x}
    :param x: a binary string
    :param t: a binary trie
    :return: the predecessor of x in t.
    """
    ix = int(x,2) # the integer value of x
    u = t
    w = len(x)
    i = 0
    while i < w :
        c = (ix>>(w-i-1)) & 1
        if not u.child[c]:
            break
        u = u.child[c]
    if i == w:
        return u.val
    u = u.jump.c or u.jump.next.c
    return u