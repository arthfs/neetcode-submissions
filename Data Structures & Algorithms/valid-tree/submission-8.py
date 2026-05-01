def dfs(source):
   
    global seen 
    global seen2
    global ref
    global cycle
    
    
    global stack

    if cycle:
        return
    
    
    for neighboor in ref.get(source, []):
        if seen.get( tuple( sorted([neighboor, source]))) == None:
            seen2[neighboor] = True 
            seen [ tuple(sorted([neighboor, source])) ] = True

            try:
                c = stack.index(neighboor)
            except:
                c = -1
            
            if c!=-1:
                cycle = True 
                return
            stack.append(neighboor)
            dfs(neighboor)

      
    stack.remove(source)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        global ref
        ref = dict()
    
        global seen
        seen = dict()

        global seen2
        seen2 = dict()

        global cycle
        cycle = False

        global stack
        
        if edges == []:
            return True
            
        for edge in edges:
            try:
                ref[edge[0]].append(edge[1])
            except:
                ref[edge[0]] = [edge[1]]

            try:
                ref[edge[1]].append(edge[0])
            except:
                ref[edge[1]] = [edge[0]]
        
        source = list(ref.keys())[0]
        stack = [source]
        seen2[source] = True
        dfs(source)
        return n == len(seen2.items()) and not cycle
        