class IsEmptyError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

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
            self.tail = new
            self.size += 1
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = self.tail
            return
        self.tail = new
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IsEmptyError("Queue is empty")
        result = self.head.element
        self.head = self.head.next
        self.size -= 1
        return result

    def __str__(self):
        str = "[]"
        if self.is_empty():
            return str
        itr = self.head
        str = "[ "
        while itr:
            str+= f"{itr.element} "
            itr = itr.next
        str += "]"
        return str

if __name__ == "__main__":
    queue = QueueLL()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue)
    print(len(queue))
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(len(queue))
    print(queue)
