from typing import List
from collections import defaultdict


class Solution:
    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        prerequisiteDict = defaultdict(list)
        for course, prerequisite in prerequisites:
            prerequisiteDict[course].append(prerequisite)

        result = []
        alreadyTaken = set()

        def findTrack(course: int, visited: set = set()) -> bool:
            if course in visited:
                return False
            visited.add(course)
            for preCourse in prerequisiteDict[course]:
                if not findTrack(preCourse, visited):
                    return False
            visited.remove(course)
            if course not in alreadyTaken:
                result.append(course)
                alreadyTaken.add(course)
            return True

        for n in range(numCourses):
            if not findTrack(n):
                return []

        return result
