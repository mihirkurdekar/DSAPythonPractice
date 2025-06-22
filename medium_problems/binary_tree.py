'''
Problem: Given a binary tree, find the lowest common ancestor of two nodes.
Example:
Code
    1
   / \
  2   3
 / \
4   5
Output: 2 (LCA of nodes 4 and 5)
'''
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    # Base case: if root is None, return None
    if not root:
        return None

    # If either p or q matches the root's value, return root
    if root.value == p or root.value == q:
        return root

    # Recur for left and right subtrees
    left_lca = lowest_common_ancestor(root.left, p, q)
    right_lca = lowest_common_ancestor(root.right, p, q)

    # If both left and right LCA are not None, then p and q are found in different subtrees
    if left_lca and right_lca:
        return root

    # Otherwise, return the non-null child (either left or right)
    return left_lca if left_lca else right_lca


# Example usage
if __name__ == "__main__":
    # Constructing the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    p = 4
    q = 5
    lca = lowest_common_ancestor(root, p, q)

    if lca:
        print("Lowest Common Ancestor of nodes", p, "and", q, "is:", lca.value)  # Output: 2
    else:
        print("Lowest Common Ancestor not found.")