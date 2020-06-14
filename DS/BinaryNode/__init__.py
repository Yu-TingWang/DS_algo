class Node:
    def __init__(self, key: int, value=None):
        self.key = key
        self.value = value
        self.right = self.left = None
        self.height = 0


    def __str__(self):
        result = ""
        result += str(self.key)
        if self.value:
            result += ", " + str(self.value)
        return result




if __name__ == "__main__":
    n = Node(0)
    print(n)