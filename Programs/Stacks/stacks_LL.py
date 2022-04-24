class IsEmptyError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class StackLL:
    class Node:
        def __init__(self,data,next = None):
            self.data = data
            self.next = next
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self,element):
        self.head = self.Node(element,self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IsEmptyError("The stack is empty")
        result = self.head.data
        self.head = self.head.next
        return result

    def top(self):
        if self.is_empty():
            raise IsEmptyError("The stack is empty")
        return self.head.data

    def __str__(self):
        str = "[]"
        if self.is_empty():
            return str
        itr = self.head
        str = "[ "
        while itr:
            str+= f"{itr.data} "
            itr = itr.next
        str += "]"
        return str


if __name__ =="__main__":
    stack = StackLL()
    stack.push(2)
    stack.push(3)
    stack.push(8)
    stack.pop()
    print(stack.top())
    print(stack)

