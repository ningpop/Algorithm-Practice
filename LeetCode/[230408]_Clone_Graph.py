"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None: return None
        node_list = {node.val : Node(node.val)}
        queue = deque([node])
        while queue:
            pop_node = queue.popleft()
            current_node = node_list[pop_node.val]
            for n in pop_node.neighbors:
                if n.val not in node_list.keys():
                    node_list[n.val] = Node(n.val)
                    queue.append(n)
                current_node.neighbors.append(node_list[n.val])
        
        return node_list[node.val]