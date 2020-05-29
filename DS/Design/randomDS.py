"""
Design a data structure such that remove and insert only takes O(1) time.
and random_remove, will randomly remove an element where each element has the same probability to be removed
"""


from pprint import PrettyPrinter

class RANDOM_DS:
    def __init__(self):
        self.dict = {}  # maps from value to index in self.array
        self.array = []

    def insert(self,value):
        if value in self.dict:
            self.dict[value] = self.dict.size # put the value, index pair into the map
            self.array.append(value)

    def remove(self, value):
        if value in self.dict:
            index = self.dict[value]
            if index == self.dict.size - 1:
                self.array.pop()
            else:
                # replace with the last element
                self.array[index] = self.array[-1]
                # throw away the last element
                self.array.pop()
            # remove the value,index pair from the map
            del self.dict[value]

    def remove_random(self):
        length = len(self.array)
        import random
        from random import randrange
        index = randrange(0, length)
        value = self.array[index]
        self.remove(value)

    def __str__(self):
        # https://stackoverflow.com/questions/44689546/how-to-print-out-a-dictionary-nicely-in-python/44689627
        import pprint
        pp = PrettyPrinter(self.dict)
        return self.array, pp


if __name__ == "__main__":
    test1 = RANDOM_DS()
    test1.insert(2)
    test1.insert(4)
    test1.insert(3)
    print(test1)
    test1.remove(5)
    print(test1)
    test1.remove_random()
    print(test1)