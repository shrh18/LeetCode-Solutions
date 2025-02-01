class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for src, dest in dislikes:
            graph[src].append(dest)
            graph[dest].append(src)
            
        colors = defaultdict(str)
        visited = defaultdict(bool)

        def dfs(node, colors, visited, prevC):
            visited[node] = True
            if colors[node] is "":
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

        for src, dests in graph.items():
            if not visited[src]:
                if not dfs(src, colors, visited, None):
                    return False
        return True