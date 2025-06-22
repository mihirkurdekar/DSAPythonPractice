'''
Problem: Given a queue of integers, find the maximum element in each window of size k.
Example: q = [1, 2, 3, 4, 5], k = 3
Output: [3, 4, 5] (maximum element in each window)
'''

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

    def size(self):
        return len(self.items)

def max_in_sliding_window(q, k):
    if not q or k <= 0:
        return []


    max_elements = []
    deq = Queue()  # This will store indices of elements in the current window
    for i in range(len(q)):
        # Remove elements not in the current window
        while not deq.is_empty() and deq.peek() <= i - k:
            deq.dequeue()

        # Remove elements smaller than the current element from the back of the deque
        while not deq.is_empty() and q[deq.peek()] < q[i]:
            deq.dequeue()

        # Add the current element's index to the deque
        deq.enqueue(i)

        # If we have filled at least k elements, add the maximum to the result
        if i >= k - 1:
            max_elements.append(q[deq.peek()])

    return max_elements


# Example usage
if __name__ == "__main__":
    q = [1, 2, 3, 4, 5]
    k = 3
    result = max_in_sliding_window(q, k)
    print("Maximum elements in each window of size", k, "are:", result)  # Output: [3, 4, 5]