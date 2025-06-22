###Problem: Given a singly linked list, find the middle element.
#Example: 1 -> 2 -> 3 -> 4 -> 5
#Output: 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1, 6):
        ll.append(i)
    ll.print_list()
    middle_element = ll.find_middle()
    print(f"The middle element of the linked list is: {middle_element}")