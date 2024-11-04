class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        dep = {c:[] for c in range(numCourses)}
        visited, path = set(), set()
        ret = []
        for c,d in prerequisites:
            dep[c].append(d)
        
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for cr in dep[course]:
                if not dfs(cr):
                    return False
            path.remove(course)
            visited.add(course)
            ret.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return ret