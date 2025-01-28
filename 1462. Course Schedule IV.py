class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        dic = {}
        dicN = defaultdict(set)

        for pre, course in prerequisites:
            if course in dic:
                dic[course].add(pre)
            else:
                gg = set()
                gg.add(pre)
                dic[course] = gg

        for course, pre in dic.items():
            visited = [False]*numCourses
            q = deque(list(pre))
            while q:
                prereq = q.popleft()
                dicN[course].add(prereq)
                if not visited[prereq]:
                    visited[prereq] = True
                    q.extend(list(dic[prereq])) if prereq in dic else None
                    
        ret = []

        for pre, course in queries:
            ret.append(True) if pre in dicN[course] else ret.append(False)
                
        return ret


        
