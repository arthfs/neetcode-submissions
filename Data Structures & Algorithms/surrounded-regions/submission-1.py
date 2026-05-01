class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = []
        seen = dict()

        n = len(board)
        m = len(board[0])
        
        queue2 = []
        for i in range(n):
            if board[i][0] == 'O':
                    seen[(i, 0 )] = True
                    queue2.append((i, 0))
            
            if board[i][m-1] == 'O':
                    seen[(i, m-1 )] = True
                    queue2.append((i, m-1))
        
        for j in range(m):
            if board[0][j] == 'O':
                    seen[(0, j )] = True
                    queue2.append((0, j))
            
            if board[n-1][j] == 'O':
                    seen[(n-1, j )] = True
                    queue2.append((n-1, j))

        #unbounded
        while queue2!= []:
            source = queue2.pop(0)
            neighboors = []

            neighboors.append((source[0], source[1] + 1))
            neighboors.append((source[0], source[1] - 1))
            neighboors.append((source[0] + 1, source[1]))
            neighboors.append((source[0] - 1, source[1]))

            for neighboor in neighboors:
                if neighboor[0] >= 0 and neighboor[0] <= n - 1 and \
                 neighboor[1] >= 0 and neighboor[1] <= m - 1 \
                  and seen.get(neighboor) == None \
                  and board[neighboor[0]] [neighboor[1]] == 'O' :
                   
                    seen[neighboor] = True
                    queue2.append(neighboor)


        #bounded

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if seen.get((i,j )) == None and board[i][j] == 'O' :
                    seen[(i,j )] = True
                    queue.append((i, j))

        while queue!= []:
            source = queue.pop(0)
            board[source[0]] [source[1]] = 'X'
            neighboors = []

            neighboors.append((source[0], source[1] + 1))
            neighboors.append((source[0], source[1] - 1))
            neighboors.append((source[0] + 1, source[1]))
            neighboors.append((source[0] - 1, source[1]))

            for neighboor in neighboors:
                if seen.get(neighboor) == None and\
                 board[neighboor[0]] [neighboor[1]] == 'O' and \
                 neighboor[0] > 0 and neighboor[0] < n - 1\
                  and neighboor[1] > 0 and neighboor[1] < m - 1:
                   
                    seen[neighboor] = True
                    queue.append(neighboor)
                
            
