from collections import defaultdict

def solve(source,ref):
    global seen
    global edges_to
    global cycle

    for neighboor in ref.get(source,[]):
        if seen.get(neighboor) == None :
            seen[neighboor] = True
            edges_to[neighboor] = source
            if source<neighboor:
                solve(neighboor,ref)
        elif seen.get(neighboor) != None and source<neighboor:
            if edges_to.get(neighboor)!=None and edges_to.get(neighboor)!=source:
                cycle = True
                print(source,neighboor,seen)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        global cycle
        cycle = False
        global seen
        seen = dict()
        global edges_to
        edges_to = dict()
        ref = defaultdict(list)
        
        for edge in edges:
            if edge[1] == edge[0]:
                return False
            ref[edge[1]].append(edge[0])
            ref[edge[0]].append(edge[1])

        for a in set(range(n)).difference(set(ref.keys())):
            ref[a] = []
        
        seen[0] = True
        solve(0,ref)

        return not cycle and n == len(seen.keys()) 
