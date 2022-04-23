class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_at_index(self, index, data):
        if index < 0 or index > self.length():
            raise IndexError("Index is out of bound")
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self,data_after,data_insert):
        count = 0
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == data_after:
            self.head.next = Node(data_insert,self.head.next)
            return
        itr = self.head
        while itr.next:
            if itr.data == data_after:
                itr.next = Node(data_insert,itr.next.next)
                count += 1
                break
            itr = itr.next
        if count == 0:
            if itr.data == data_after:
                itr.next = Node(data_insert)
                return
            print("Data not in the linked list")

    def remove_first(self):
        if self.head is None:
            print("Nothing to remove")
            return
        self.head = self.head.next

    def remove_at(self, index):
        if index < 0 or index > self.length() - 1:
            raise IndexError("Index is out of bound")
        count = 0
        if index == 0:
            self.remove_first()
            return
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def remove_by_value(self,data):
        count = 0
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                count += 1
                break
            itr = itr.next
        if count == 0:
            print("Data not in the linked list")
    def print(self):
        if self.head is None:
            print("There is no element in the linked list")
            return
        itr = self.head
        string = " "
        while itr:
            string += itr.data + "-->"
            itr = itr.next
        print(string)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


if __name__ == "__main__":
    list_one = LinkedList()
    list_one.insert_at_beginning("Jayesh")
    list_one.insert_at_beginning("Piyush")
    list_one.insert_at_beginning("Shrikant")
    list_one.insert_at_end("Shakti")
    list_one.insert_values(["Sakshi", "Ruchi", "Achal"])
    list_one.print()
    list_one.remove_first()
    list_one.print()
    list_one.insert_at_index(2, "Priya")
    list_one.print()
    list_one.remove_at(2)
    list_one.print()
    list_one.remove_by_value("Sakshi")
    list_one.print()
    list_one.insert_after_value("Achal","Jayesh")
    list_one.print()
    print(f"Length is, {list_one.length()}")
