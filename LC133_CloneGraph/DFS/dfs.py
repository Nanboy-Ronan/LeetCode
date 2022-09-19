"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # DFS
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        nodeCopy = self.dfs(node, visited)
        return nodeCopy
    
    def dfs(self, node, visited):
        if node is None:
            return None
        
        if node.val in visited:
            return visited[node.val]

        copyNode = Node(node.val, [])
        visited[node.val] = copyNode
        
        for neighbor in node.neighbors:
            copyNeighber = self.dfs(neighbor, visited)
            copyNode.neighbors.append(copyNeighber)
        return copyNode