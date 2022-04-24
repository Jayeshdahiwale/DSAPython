class QueueLL:
    class Node:
        def __init__(self,element,next = None):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self,element):
        new = self.Node(element)
        if self.is_empty():
           self.head = new
        else:
            self.tail.next = new
            self.size += 1
            return
        self.tail = new
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise 