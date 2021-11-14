# Question 2 - delete a specific value from a queue
class Queue(object):
    inner_list = []
    counter = 0
    
    def enqueue(self, value):
        self.inner_list.insert(self.counter, value)
        self.counter = self.counter + 1
        
    def dequeue(self):
        self.counter = self.counter - 1
        value = self.inner_list.pop(0)
        return value
    
    def delete(self, value):
        tmp = []
        for i in range(len(self.inner_list)):
            tmp.append(self.dequeue())
        j = 0
        while j < len(tmp):
            if tmp[j] == value:
                tmp.pop(j)
                break
            j += 1
        for k in range(len(tmp)):
            self.enqueue(tmp[k])

# test case
obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)
print(obj.inner_list)

obj.delete(7)
print(obj.dequeue())
print(obj.inner_list)