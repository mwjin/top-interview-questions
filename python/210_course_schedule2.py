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

        for n in range(numCourses):
            track = [n]
            discovered = {n}

            while track:
                if prerequisiteDict[track[-1]]:
                    prerequisite = prerequisiteDict[track[-1]].pop()
                    if prerequisite in discovered:
                        return []
                    track.append(prerequisite)
                    discovered.add(prerequisite)
                else:
                    course = track.pop()
                    discovered.remove(course)

                    if course not in alreadyTaken:
                        result.append(course)
                        alreadyTaken.add(course)

        return result
