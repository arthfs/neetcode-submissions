def dfs(source, grid):
    global sol
    global seen
    global n
    global m
    global current

    neighboors = []
    if source[0]-1 >=0:
        neighboors.append((source[0] - 1, source[1]))

    if source[0] + 1 <n:
        neighboors.append((source[0] + 1, source[1]))

    if source[1] + 1 <m:
        neighboors.append((source[0] , source[1] + 1))

    if source[1] - 1 >=0:
        neighboors.append((source[0] , source[1] - 1))

    for neighboor in neighboors:
        if seen.get(neighboor) == None and grid[neighboor[0]] [neighboor[1]] == 1:
            current+=1
            sol = max([sol, current])
            seen[neighboor] = True
            dfs(neighboor, grid)

   

import sys
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global sol
        sol = -sys.maxsize

        global n
        n = len(grid)

        global m 
        m = len(grid[0])

        global seen
        seen = dict()

        global current
        current = 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and seen.get((i,j)) == None:
                    seen[(i,j)] = True
                    current = 1
                    sol = max([sol, current])
                    dfs((i,j), grid)
        
        return 0 if sol == -sys.maxsize else sol
