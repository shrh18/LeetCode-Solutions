class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep = {}
        for c,d in prerequisites:
            if c in dep:
                dep[c].append(d)
            else:
                dep[c] = [d]
        print(dep)
        def bfs(key,arr,visited):
            for k in arr:
                if k in dep:
                    if key in dep[k]:
                        return False

                if k not in visited:
                    if key==k:
                        return False
                    if k in dep:
                        visited.append(k)
                        return bfs(key,dep[k],visited)
            return True

        visited = []       
        for k,v in dep.items():   
            if not bfs(k,v,visited):
                return False
            visited.append(k)
        return True
                 
