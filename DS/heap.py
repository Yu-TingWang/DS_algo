class minHeap():
    def __init__(self):
        self.array =[None]
        self.size=0
    
    def isEmpty(self):
        return self.size==0
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.array[1]

    def extract(self): # this take O(logn)
        if self.isEmpty():
            return None
        else:
            result = self.array[1]
            # replace head with the last leaf
            bottom = self.array.pop()
            self.size -=1
            self.array[1] = bottom
            # reorganize the heap
            self.ToptoBottom(1)
        return result

    def ToptoBottom(self,index):
        # bubble down
        left=index*2
        right=index*2+1
        # if this node has no child
        if self.size<left:
            return
        # if this node has only one child
        if self.size==left:
            if self.array[index]>self.array[left]:
                # swap them
                temp = self.array[index]
                self.array[index] = self.array[left]
                self.array[left] = temp
            return
        # if this node has both childred
        else: # get the smallest child
            if self.array[right]<self.array[left]:
                smallest_child=right
            else:
                smallest_child =left
            if self.array[index]>self.array[smallest_child]:
                #swap 
                temp = self.array[index]
                self.array[index] = self.array[smallest_child]
                self.array[smallest_child] = temp
        self.ToptoBottom(smallest_child)


    def insert(self, value):# this takes O(logn)
        self.array.append(value)
        self.size +=1
        self.BottomtoTop(self.size)

    def BottomtoTop(self,index):
        # bubble up
        parent = index//2
        if index<=1:
            return
        if self.array[index]<self.array[parent]:
            # then swap the parent and child
            temp = self.array[index]
            self.array[index] = self.array[parent]
            self.array[parent] = temp

        self.BottomtoTop(parent)

    
    def delete(self):
        self=None

    def bfs(self):
        print(self.array)

if __name__ == "__main__":
    heap = minHeap()
    heap.insert(5)
    heap.bfs()
    heap.insert(1)
    heap.insert(4)
    heap.bfs()
    print(heap.extract())
    heap.bfs()
