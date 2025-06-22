# Problem: Given a string of parentheses, check if the parentheses are balanced.
# Example: s = "((()))"
# Output: True

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")


def is_balanced_parentheses(s):
    stack = Stack()
    parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parentheses_map.values():  # If it's an opening bracket
            stack.push(char)
        elif char in parentheses_map.keys():  # If it's a closing bracket
            if stack.is_empty() or stack.pop() != parentheses_map[char]:
                return False

    return stack.is_empty()

# Example usage
if __name__ == "__main__":
    s = "((()))"
    print(is_balanced_parentheses(s))  # Output: True

    s = "(()"
    print(is_balanced_parentheses(s))  # Output: False

    s = "{[()()]}"
    print(is_balanced_parentheses(s))  # Output: True

    s = "{[(])}"
    print(is_balanced_parentheses(s))  # Output: False