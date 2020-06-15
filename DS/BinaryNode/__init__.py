class BinaryNode:
    def __init__(self, value: int = None):
        self.val = value
        self.right = self.left = None
        self.height = 1

    def __str__(self):
        result = ""
        result += str(self.value)
        result += self.left.__str__
        result += self.right.__str__
        return result

    def reset_height(self)->int:
        """
        Recalculate the height by assessing right and left child height.
        :return: the height of this node
        """
        if not self:
            return 0
        return 1+max(self.left.height if self.left else -1, self.right.height if self.right else -1)

if __name__ == "__main__":
    n = BinaryNode(0)
    print(n)
