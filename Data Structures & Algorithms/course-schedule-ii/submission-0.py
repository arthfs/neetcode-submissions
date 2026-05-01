from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ref = defaultdict(list)
        for p in prerequisites:
            ref[p[0]].append(p[1])
        
        for i in range(numCourses):
            if ref.get(i) == None:
                ref[i] = []

        taken = dict()
        sol = []

        while len(taken)!= numCourses:
            changed = False
            for course in ref.items():
                if taken.get(course[0]) == None:
                    for pre in course[1]:
                        if taken.get(pre) == None:
                            break
                    else:
                        changed = True
                        sol.append(course[0])
                        taken[course[0]] = True

            if not changed:
                return []
        return sol