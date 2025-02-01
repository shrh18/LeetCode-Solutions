class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [None]*n
        visited = [False]*n

        def dfs(node, colors, visited, prevC):
            visited[node] = True
            if colors[node] is None:
                colors[node] = "w" if prevC == "b" else "b"
            else:
                if colors[node] == prevC:
                    return False
        
            for n in graph[node]:
                if not visited[n]:
                    if not dfs(n, colors, visited, colors[node]):
                        return False
                elif colors[n] == colors[node]:
                    return False

            return True


        
        for src in range(len(graph)):
            if not visited[src]:
                if not dfs(src, colors, visited, None):
                    return False
        return True