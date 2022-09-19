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
    # BFS
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited = {}
        queue = deque()
        newNode = Node(node.val, [])
        visited[node.val] = newNode
        queue.append(node)
        while len(queue) != 0:
            length  = len(queue)
            for i in range(length):
                n = queue.popleft()
                for neighbor in n.neighbors:
                    if neighbor.val not in visited:
                        nodeCopy = Node(neighbor.val, [])
                        visited[neighbor.val] = nodeCopy
                        visited[n.val].neighbors.append(nodeCopy)
                        queue.append(neighbor)
                    else:
                        visited[n.val].neighbors.append(visited[neighbor.val])
        return newNode