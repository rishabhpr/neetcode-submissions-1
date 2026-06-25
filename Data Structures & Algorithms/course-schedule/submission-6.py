class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre_map ={ course : [] for course in range(numCourses)}

        for course, pre_req in prerequisites:
            pre_map[course].append(pre_req)
        
        visiting  = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if not pre_map[course]:
                return True
            
            visiting.add(course)

            for pre_req in pre_map[course]:
                if not dfs(pre_req):
                    return False
            
            visiting.remove(course)

            pre_map[course] = []

            return True
        
        for num in range(numCourses):
            if not dfs(num):
                return False
        
        return True

        