class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp =self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(5)
my_linked_list.append(3)
my_linked_list.append(7)
my_linked_list.append(9)

print(my_linked_list.get(3).value)
my_linked_list.print_list()
my_linked_list.set_value(3, 15)
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    5

"""