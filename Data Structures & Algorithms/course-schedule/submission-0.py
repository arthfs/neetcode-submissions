class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ref = dict()
        
        for p in prerequisites:
            try:
                ref[ p[0] ] [1].append(p[1])
            
            except:
                ref[ p[0] ] = [[], [p[1]]] 

            try:
                ref[ p[1] ] [0].append(p[0])
            except:
                ref[ p[1] ] = [[p[0]], []]

        for i in range(numCourses):
            if ref.get(i) == None:
                ref[i] = [[], []]

        taken = dict()
        n = 0

        while n!= numCourses:
            changed = False
            for course, prereq in ref.items():
                if prereq[1] == [] and taken.get(course) == None:
                    taken[course] = True
                    changed = True
                    n+=1
                    for dependent in prereq[0]:
                        ref[dependent] [1].remove(course)
            if not changed:
                return False
        
        return True