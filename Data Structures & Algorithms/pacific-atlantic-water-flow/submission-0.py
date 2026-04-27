def get_neighboors(source, heights, n, m):
    neighboors = []

    #up
    if source[0]-1 >= 0 and  heights[ source[0]-1] [source[1]] >= heights[ source[0]] [source[1]]:
        neighboors.append((source[0]-1, source[1]))

    #down
    if source[0]+1 < n and  heights[ source[0]+1] [source[1]] >= heights[ source[0]] [source[1]]:
        neighboors.append((source[0]+1, source[1]))

    #left
    if source[1]-1 >= 0 and  heights[ source[0]] [source[1]-1] >= heights[ source[0]] [source[1]]:
        neighboors.append((source[0], source[1]-1))

    #right
    if source[1]+1 < m and  heights[ source[0]] [source[1]+1] >= heights[ source[0]] [source[1]]:
        neighboors.append((source[0], source[1]+1))
    
    return neighboors

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        sol = set()
        seen = dict()

        pacific = dict()

        atlantic = dict()

        queue = []
        n = len(heights)
        m = len(heights[0])

        for i in range(n):
            pacific[(i, 0)] = True
            atlantic[i, m-1] = True
            if ((i,0)) not in queue:
                queue.append((i,0))
            
            if ((i, m-1)) not in queue:
                queue.append((i, m-1))

        for j in range(m):
            pacific[(0, j)] = True 
            atlantic[(n-1, j )] = True

            if ((0, j)) not in queue:
                queue.append((0, j))

            if ((n-1, j)) not in queue:
                queue.append((n-1, j))

        #print(queue)
        while queue!=[]:
            source = queue.pop(0)
            if pacific.get(source, False) and atlantic.get(source, False):
                sol.add(source)

            neighboors = get_neighboors(source, heights, n, m)
            for neighboor in neighboors:
                if (not pacific.get(neighboor, False) and pacific.get(source, False)) \
                    or (not atlantic.get(neighboor, False) and atlantic.get(source, False)):
                    
                    queue.append(neighboor)

                atlantic[neighboor] = atlantic.get(neighboor, False) or atlantic.get(source, False)
                pacific[neighboor] = pacific.get(neighboor, False) or pacific.get(source, False)

        return list(sol)