'''
Problem: Given a string of operators and operands, evaluate the postfix expression.
Example: s = "3 4 + 2 *"
Output: 14 (evaluation of postfix expression)
'''

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

    def size(self):
        return len(self.items)


def evaluate_postfix(expression):
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():  # If the token is an operand (number)
            stack.push(int(token))
        else:  # The token is an operator
            b = stack.pop()  # Pop the top two elements
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            else:
                raise ValueError(f"Unknown operator: {token}")
            stack.push(result)  # Push the result back onto the stack

    return stack.pop()  # The final result should be the only element left in the stack


# Example usage
if __name__ == "__main__":
    expression = "3 4 + 2 *"
    result = evaluate_postfix(expression)
    print("Result of postfix expression:", result)  # Output: 14