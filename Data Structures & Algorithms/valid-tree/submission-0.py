class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = {node: [] for node in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nbr in graph[node]:
                dfs(nbr)
        
        dfs(0)
        return len(visited) == len(graph)


        