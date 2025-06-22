'''
Problem: Given a singly linked list, detect and remove a cycle.
Example:
Code
1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle)
Output: 1 -> 2 -> 3 -> 4 -> 5 (cycle removed)
'''

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def detect_and_remove_cycle(self):
        # This function detects and removes a cycle in the linked list
        slow = self.head
        fast = self.head
        has_cycle = False
        # Step 1: Detect cycle using Floyd's Tortoise and Hare algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        if not has_cycle:
            print("No cycle detected.")
            return
        # Step 2: Find the start of the cycle
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        # Step 3: Find the last node in the cycle and remove the cycle
        cycle_start = slow
        while fast.next != cycle_start:
            fast = fast.next
        fast.next = None
        print("Cycle removed.")
        # Print the list after removing the cycle
        self.print_list()




# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    # Creating a cycle for demonstration
    ll.head.next.next.next.next.next = ll.head.next  # 5 -> 3 (cycle)

    print("Linked List before removing cycle:")
    ll.print_list()

    ll.detect_and_remove_cycle()

    print("Linked List after removing cycle:")
    ll.print_list()