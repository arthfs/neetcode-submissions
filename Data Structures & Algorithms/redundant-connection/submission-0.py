from collections import defaultdict
def getCycle(start, end):
    global parent 
    global cycles
    cycles.append(tuple(sorted([start, end])))
    while start!= end:
        #print((start, parent[start]))
        cycles.append(tuple(sorted([start, parent[start]])))
        start = parent[start]
        

def dfs(source):
    global seen 
    global stack 
    global cycle 
    global parent

    if cycle :
        return

    for neighboor in ref[source]:
       
        if seen.get (tuple(sorted([source, neighboor]))) == None:
            if neighboor in stack:
               
                getCycle(source, neighboor)
                seen[(tuple(sorted([source, neighboor]))) ] = True
                cycle = True 
                return 
                
            parent[neighboor] = source
            stack.append(neighboor)
            seen[(tuple(sorted([source, neighboor]))) ] = True
            dfs(neighboor)
    stack.remove(source)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        global stack
        stack  = []

        global seen
        seen = dict()

        global cycleEdge
        cycleEdge = []

        global parent
        parent = dict()

        global ref 
        ref = defaultdict (list)

        global cycles
        cycles = []

        global cycle 
        cycle = False

        for edge in edges:
            u,v = edge 
            ref[u].append(v)
            ref[v].append(u)

        source = list(ref.keys())[0]
        stack.append(source)
        dfs(source)
 
        for i in range(len(edges) - 1, -1, -1):
            if tuple(edges[i]) in cycles:
                return(edges[i])
            
            