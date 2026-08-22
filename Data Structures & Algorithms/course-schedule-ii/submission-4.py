class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i : [] for i in range(numCourses)}

        for course, pre in prerequisites:
            pre_map[course].append(pre)

        cycle = set()
        done = set()

        def dfs(course):
            if course in cycle:
                return False

            if course in done:
                return True

            cycle.add(course)

            for pre in pre_map[course]:
                if not dfs(pre): return False
            cycle.remove(course)
            done.add(course)
            output.append(course)
            return True

        output = []
        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return output