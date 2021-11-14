# Question 7 - Tri-tree
class Node(object):
    # create the data structure
    def __init__(self, data):
        self.small = None
        self.big = None
        self.toobig = None
        self.data = data
    
    # create the insert function (only way I could think to do this is over 15 lines)
    def insert(self, data): # what you are comparing to
        if self.data: # what you already have
            if data < self.data:
                if self.small is None: 
                    self.small = Node(data)
                else:
                    self.small.insert(data)
            elif 10 > data - self.data >= 0:
                if self.big is None:
                    self.big = Node(data)
                else:
                    self.big.insert(data)
            elif data - self.data >= 10:
                if self.toobig is None:
                    self.toobig = Node(data)
                else:
                    self.toobig.insert(data)
        else:
            self.data = data
        
    # create the traversal function - small child, then root node, then big child, then too big child
    
    # traversal without returning anything
    def traversal(self):
        if self.small:
            self.small.traversal()
        print(self.data)
        if self.big:
            self.big.traversal()
        if self.toobig:
            self.toobig.traversal()
    
    # inner traversal, only works with delete function or if passed empty list
    def traversal2(self, tmp):
        if self.small:
            self.small.traversal2(tmp)
        tmp.append(self.data)
        if self.big:
            self.big.traversal2(tmp)
        if self.toobig:
            self.toobig.traversal2(tmp)
        return tmp
    
    # inner traversal, only works with delete function or if passed empty list
    def delete(self, data):
        tmp = []
        x = self.traversal2(tmp)
        i = 0
        while i < len(x):
            if x[i] == data:
                x.pop(i)
                break
            i += 1
        print(x)
        self.small = None
        self.big = None
        self.toobig = None
        self.data = None
        for i in range(len(x)):
            self.insert(x[i])

# test cases
root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)

# traversal
print("Tree before delete: ")
root.traversal()

root.delete(20)

print("Tree after delete: ")
root.traversal()