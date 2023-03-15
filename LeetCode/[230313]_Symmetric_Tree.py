# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

EOC = 1001

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        unit_node = []
        while queue:
            # print(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    unit_node.append(TreeNode(val=EOC))
                else:
                    unit_node.append(node.val)
                # print(node)
                if node.val == EOC:
                    continue

                if node.left is None:
                    queue.append(TreeNode(val=EOC))
                else:
                    queue.append(node.left)
                
                if node.right is None:
                    queue.append(TreeNode(val=EOC))
                else:
                    queue.append(node.right)

            center = len(unit_node) // 2
            first = unit_node[:center]
            second = unit_node[center:][::-1]
            if len(unit_node) % 2 == 1:
                first = unit_node[:center + 1]

            # print(f'\n>>> unit_node: {unit_node}')
            # print(f'>>> first: {first}')
            # print(f'>>> second: {second}\n')

            if first != second:
                return False
            unit_node.clear()
            continue
        
        return True