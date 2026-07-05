class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {node: [] for node in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        components = 0

        def dfs(node):
            if node in visited:
                return
            
            # lets process node

            visited.add(node)

            for nbr in graph[node]:
                dfs(nbr)
        
        for node in range(n):
            if node not in visited:
                components +=1
                dfs(node)
        
        return components

        