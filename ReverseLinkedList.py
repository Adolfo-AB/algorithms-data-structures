class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        previous = None
        current = self.head
        
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

linked = LinkedList()
linked.push(1)
linked.push(2)
linked.push(3)
linked.push(4)
linked.push(5)

print("Initial linked list.")
linked.print_list()
print("Reversed linked list.")
linked.reverse()
linked.print_list()
