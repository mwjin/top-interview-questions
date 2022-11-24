from typing import List
from collections import defaultdict


class Solution:
    def canFinish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        discovered = set()

        for course in range(numCourses):
            path = [course]

            while path:
                discovered.add(path[-1])

                if graph[path[-1]]:
                    prerequisite = graph[path[-1]].pop()
                    if prerequisite in discovered:
                        return False
                    path.append(prerequisite)
                else:
                    discovered.remove(path.pop())

        return True


print(Solution().canFinish(2, [[1, 0]]))
