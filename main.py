class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_level_sum(root):
    if root is None:
        return None, 0
    from collections import deque
    q = deque([root])
    best_level = 0
    best_sum = root.value
    level = 0
    while q:
        s = 0
        for _ in range(len(q)):
            node = q.popleft()
            s += node.value
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if s > best_sum:
            best_sum = s
            best_level = level
        level += 1
    return best_level, best_sum


if __name__ == "__main__":
    left = TreeNode(5, TreeNode(4), TreeNode(1))
    right = TreeNode(7)
    root = TreeNode(10, left, right)
    print(max_level_sum(root))
