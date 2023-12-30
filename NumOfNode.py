from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes_at_level(root, target_level):
    if root is None:
        return 0

    level = 0
    queue = deque([(root, level)])
    count_at_target_level = 0

    while queue:
        current_node, current_level = queue.popleft()

        if current_level == target_level:
            count_at_target_level += 1

        if current_node.left:
            queue.append((current_node.left, current_level + 1))
        if current_node.right:
            queue.append((current_node.right, current_level + 1))

    return count_at_target_level

# Construct a binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Set the target level
target_level = 2

# Count the number of nodes at the target level
result = count_nodes_at_level(root, target_level)
print(f"Number of nodes at level {target_level}: {result}")
