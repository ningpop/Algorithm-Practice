class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        v: int = len(isConnected)
        connected_info = []
        for i in range(v):
            for j in range(i + 1, v):
                if isConnected[i][j] == 1:
                    connected_info.append((i, j))

        parent = [0] * (v)
        for i in range(v):
            parent[i] = i

        for a, b in connected_info:
            print(a, b)
            self.union_parent(parent, a, b)
        for i in range(v):
            self.find_parent(parent, i)
        result = list(set(parent))
        return len(result)
    
    def find_parent(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find_parent(parent, parent[x])
        return parent[x]
    
    def union_parent(self, parent, a, b):
        a = self.find_parent(parent, a)
        b = self.find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b