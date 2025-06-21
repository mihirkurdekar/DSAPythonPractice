# Problem: Given a binary tree, find the sum of all nodes.
# Example:
# Code
#     1
#    / \
#   2   3
#  / \
# 4   5
# Output: 15 (1 + 2 + 3 + 4 + 5)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value, end=" ")
        if self.right:
            self.right.print_tree()


# Function to calculate the sum of all nodes in a binary tree
def sum_of_nodes(node):
    if node is None:
        return 0
    return node.value + sum_of_nodes(node.left) + sum_of_nodes(node.right)

# Example usage
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.insert(2)
    root.insert(4)
    root.insert(3)
    root.insert(5)

    # Print the tree
    print("Binary Tree (In-Order Traversal):")
    root.print_tree()  # Output: 4 2 5 1 3

    # Calculate the sum of all nodes
    total_sum = sum_of_nodes(root)
    print("\nSum of all nodes:", total_sum)  # Output: 15