from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: optional[TreeNode]) -> bool:
        is_even_index = True
        nodes = deque()
        nodes.append(root)

        while nodes:
            if len(nodes) == 1:
                if is_even_index:
                    if nodes[0].val % 2 == 0:
                        return False
                else:
                    if nodes[0].val % 2 != 0:
                        return False
            else:
                for i in range(len(nodes) - 1):
                    if is_even_index:
                        if nodes[i].val % 2 == 0 or nodes[i + 1].val % 2 == 0:
                            return False
                        if nodes[i].val >= nodes[i + 1].val:
                            return False
                    else:
                        if nodes[i].val % 2 != 0 or nodes[i + 1].val % 2 != 0:
                            return False
                        if nodes[i].val <= nodes[i + 1].val:
                            return False

            count_nodes = len(nodes)
            for _ in range(count_nodes):
                curr = nodes.popleft()
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)

            is_even_index = not is_even_index

        return True
