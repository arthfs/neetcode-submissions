from collections import defaultdict
def solve(source,ref):
    global seen


    for neighboor in ref.get(source,[]):
        if seen.get(neighboor) == None:
            seen[neighboor] = True
            solve(neighboor,ref)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        global solu
        if n == 0:
            return 0
        solu = 0

        global seen
        seen = dict()
      
        ref = defaultdict(list)
        for edge in edges:
            ref[edge[0]].append(edge[1])
            ref[edge[1]].append(edge[0])
       
        for a in set(range(n)).difference(set(ref.keys())):
                ref[a] = []
       
        for i in ref.keys():
            if seen.get(i) == None:
             
                seen[i] = True
                solve(i,ref)
                solu+=1
        
        return solu