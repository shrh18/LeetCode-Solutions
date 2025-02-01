class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            
        colors = defaultdict(str)
        visited = defaultdict(bool)

        def dfs(node, colors, visited, prevC):
            visited[node] = True
            if colors[node] == "":
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

        def bfs(node):
            q = deque([(node, 1)])
            visited = {node:1}
            maxLevel = 1

            while q:
                no, level = q.popleft()
                maxLevel = max(maxLevel, level)

                for n in graph[no]:
                    if n not in visited:
                        visited[n] = level + 1
                        q.append((n, level+1))

            return maxLevel


        for src, dests in graph.items():
            if not visited[src]:
                if not dfs(src, colors, visited, None):
                    return -1

        total = 0
        visited = set()
        for src in range(1, n+1):
            if src not in visited:
                component = []
                stack = [src]
                visited.add(src)

                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)

                maxGroups = 0
                for node in component:
                    maxGroups = max(maxGroups, bfs(node))
                total += maxGroups

        return total

