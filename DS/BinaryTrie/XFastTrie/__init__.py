from DS.BinaryTrie import BinaryTrie


class XFastTrie(BinaryTrie):
    class Node:
        def __init__(self, x):
            super.__init__(x)
            self.prefix = 0  # i.e. the root-node path

    def __init__(self, w):
        """

        :param w: this height of the trie
        """
        self.height = w
        default_value = {}
        # this hash table takes the level as a key and maps to another hash table
        # the inner table takes the decimal value of the node as a key and maps to the node
        self.table = dict.fromkeys(list(range(0, w)), default_value)
        # t[0][root]=None


def _find(x: str, t: XFastTrie):
    start, end = 0, len(x) + 1
    tmp, pre = t, ""
    while end - start > 1:
        mid = (start + end) // 2
        pre = x[:mid]
        if int(pre, 2) in t.table[mid]:
            start = mid
            tmp = t.table[start][int(pre, 2)]
        else:
            end = mid
    return tmp, start


def _find(x: int, t: XFastTrie):
    start, end = 0, len(x) + 1
    ix = int(x, 2)
    tmp, pre = t, ""
    while end - start > 1:
        mid = (start + end) // 2
        pre = ix >> (t.w - mid)
        if pre in t.table[mid]:
            start = mid
            tmp = t.table[start][pre]
        else:
            end = mid
    return tmp, start


def predecessor(x: str, t: XFastTrie):
    tmp, level = _find(x, t)
    if level == 0 or level == t.height:
        return tmp
    tmp = tmp.jump
    if tmp.key < int(x, 2):
        return tmp.left
    return tmp.right


def successor(x: str, t: XFastTrie):
    tmp, level = _find(x, t)
    if level == 0 or level == t.height:
        return tmp
    tmp = tmp.jump
    if tmp.key < int(x, 2):
        return tmp.left
    return tmp.right
