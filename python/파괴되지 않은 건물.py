def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    
    diff = [[0] * (M + 1) for _ in range(N + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        value = degree if type == 2 else -degree

        diff[r1][c1] += value
        
        diff[r1][c2 + 1] -= value
        
        diff[r2 + 1][c1] -= value
        
        diff[r2 + 1][c2 + 1] += value

    for r in range(N):
        for c in range(1, M):
            diff[r][c] += diff[r][c-1]

    for c in range(M):
        for r in range(1, N):
            diff[r][c] += diff[r-1][c]

    for i in range(N):
        for j in range(M):
            board[i][j] += diff[i][j]

    for i in board:
        for j in i:
            if(j>0):
                answer+=1
            
    return answer