def solution(m, n, board):
    answer = 0

    board = [ list(row) for row in board ]

    while True:
        to_remove = set()

        for i in range(m-1):
            for j in range(n-1):
                block = board[i][j]
                if(block == "0"):
                    continue

                if(board[i+1][j] == block and board[i][j+1] == block and board[i+1][j+1] == block):
                    to_remove.add((i,j))
                    to_remove.add((i+1,j))
                    to_remove.add((i,j+1))
                    to_remove.add((i+1,j+1))
        
        if not to_remove:
            break

        answer+= len(to_remove)

        for i in to_remove:
            r,c = i
            board[r][c] = "0"
        
        for i in range(n):
            temp_col = []
            for j in range(m-1,-1,-1):
                if board[j][i] != "0":
                    temp_col.append(board[j][i])
            
            for j in range(m-1,-1,-1):
                if temp_col:
                    board[j][i] = temp_col.pop(0)
                else:
                    board[j][i] = "0"
    
    return answer