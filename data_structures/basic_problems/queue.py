# Problem: Given a queue of integers, reverse the queue.
# Example: q = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek from empty queue")


def reverse_queue(queue):
    stack = []

    # Dequeue all elements from the queue and push them onto the stack
    while not queue.is_empty():
        stack.append(queue.dequeue())

    # Pop all elements from the stack and enqueue them back to the queue
    while stack:
        queue.enqueue(stack.pop())

    return queue


# Example usage
if __name__ == "__main__":
    q = Queue()
    for i in range(1, 6):
        q.enqueue(i)

    print("Original queue:", q.items)  # Output: [1, 2, 3, 4, 5]

    reversed_q = reverse_queue(q)
    print("Reversed queue:", reversed_q.items)  # Output: [5, 4, 3, 2, 1]