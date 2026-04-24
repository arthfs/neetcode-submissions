import heapq
def solve(grid,source):
    global inf
    seen = dict()
    dist = defaultdict( lambda x: inf)
    dist[source] = 0
    seen [source] = True
    ref = []
    heapq.heappush(ref,(dist[source],source))
    while ref!=[]:
        c = heapq.heappop(ref)
        neighboors = []
        coordinate = c[1]
        if coordinate[0]>0:
            neighboors.append((coordinate[0]-1,coordinate[1]))

        if coordinate[0]<len(grid)-1:
            neighboors.append((coordinate[0]+1,coordinate[1]))

        if coordinate[1]>0:
            neighboors.append((coordinate[0],coordinate[1]-1))

        if coordinate[1]< len(grid[0])-1:
            neighboors.append((coordinate[0],coordinate[1]+1))

        for neighboor in neighboors:
            if seen.get(neighboor) == None and grid[neighboor[0]] [neighboor[1]]!= -1:
                seen[neighboor] = True 
                dist[neighboor] = c[0] +1 
                heapq.heappush(ref,(dist[neighboor],neighboor))
    
    #print(dist)
    temp = [i for i in dist.items() if grid[i[0][0]] [i[0][1]] == 0]
    try:
        return sorted(temp,key = lambda x: x[1] ) [0][1]
    except:
        pass

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        global inf
        inf = 2147483647
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == inf:
                    c = solve(grid,(i,j))
                    if c!=None:
                        grid[i][j] = c