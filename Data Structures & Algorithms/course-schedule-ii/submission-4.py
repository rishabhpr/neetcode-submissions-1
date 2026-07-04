class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        queue = deque()
        pre_map = {course : [] for course in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre_req in prerequisites:
            pre_map[pre_req].append(course)
            indegree[course] +=1
        
        # init queue
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        

        while queue:
            cur_course = queue.popleft()
            order.append(cur_course)
            for course in pre_map[cur_course]:
                indegree[course]-=1
                if indegree[course] == 0:
                    queue.append(course)
            
        if len(order) == numCourses:
            return order
        else:
            return []
        

        

        



        