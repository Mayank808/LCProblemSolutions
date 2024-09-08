from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Topo sort
        # require indegree and then a queue to bfs the graph and top sort

        edges = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            edges[b].append(a)

            indegree[a] += 1
        
        # print(indegree)
        zero_in_queue = deque([k for k in range(numCourses) if indegree[k] == 0])

        # print(zero_in_queue)
        top_sort_arr = []
        while zero_in_queue:
            course = zero_in_queue.popleft()
            top_sort_arr.append(course)

            if course not in edges:
                continue
            
            for child in edges[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    zero_in_queue.append(child)

        return top_sort_arr if len(top_sort_arr) == numCourses else []
        
