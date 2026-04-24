import heapq
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        seen = dict()
        start = None 
        n = len(grid)
        m = len(grid[0])
        dist = dict()



        ref = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    start = (i,j)
                    heapq.heappush(ref, (0, start))
        

        while ref!=[]:
            distance, c = heapq.heappop(ref)


            neighboors = []
            if c[1] +1 <m:
                neighboors.append((c[0], c[1]+1))
            
            if c[1] -1 >=0:
                neighboors.append((c[0], c[1]-1))

            if c[0] -1 >=0:
                neighboors.append((c[0]-1, c[1]))

            if c[0] +1 <n:
                neighboors.append((c[0]+1, c[1]))

            for neighboor in neighboors:
                if grid[neighboor[0]] [neighboor[1]] in [inf, 0]:
                    if distance +1 < grid[ neighboor[0]] [neighboor[1]]:
                        grid[ neighboor[0]] [neighboor[1]] = min(grid[ neighboor[0]] [neighboor[1]], distance +1)
                        heapq.heappush(ref, (grid[ neighboor[0]] [neighboor[1]], (neighboor[0],neighboor[1]) ))

    