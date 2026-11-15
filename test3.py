from collections import deque
import copy

def solution(board, commands):
    N = len(board)
    M = len(board[0])

    # 방향 매핑: 상, 우, 하, 좌
    dir_map = {1:(-1,0), 2:(0,1), 3:(1,0), 4:(0,-1)}

    def find_apps(board):
        visited = [[False]*M for _ in range(N)]
        apps = {}
        for r in range(N):
            for c in range(M):
                if board[r][c] != 0 and not visited[r][c]:
                    app_id = board[r][c]
                    q = deque([(r,c)])
                    visited[r][c] = True
                    cells = [(r,c)]
                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nr, nc = cr+dr, cc+dc
                            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and board[nr][nc]==app_id:
                                visited[nr][nc] = True
                                q.append((nr,nc))
                                cells.append((nr,nc))
                    min_r = min(x[0] for x in cells)
                    min_c = min(x[1] for x in cells)
                    max_r = max(x[0] for x in cells)
                    max_c = max(x[1] for x in cells)
                    apps[app_id] = (min_r, min_c, max_r-min_r+1, max_c-min_c+1)
        return apps

    apps = find_apps(board)

    def move(app_id, direction):
        dr, dc = dir_map[direction]
        queue = deque([app_id])
        moved = set()
        while queue:
            curr = queue.popleft()
            if curr in moved:
                continue
            moved.add(curr)
            r, c, h, w = apps[curr]

            # 이동할 영역 기록
            new_r = (r + dr) % N
            new_c = (c + dc) % M

            # 다른 앱과 겹치면 연쇄 이동
            to_move = set()
            for i in range(h):
                for j in range(w):
                    nr = (r+i+dr) % N
                    nc = (c+j+dc) % M
                    if board[nr][nc] != 0 and board[nr][nc] != curr:
                        to_move.add(board[nr][nc])
            for other in to_move:
                if other not in moved:
                    queue.append(other)

            # 이전 위치 초기화
            for i in range(h):
                for j in range(w):
                    board[(r+i)%N][(c+j)%M] = 0

            # 새 위치에 앱 배치
            for i in range(h):
                for j in range(w):
                    board[(new_r+i)%N][(new_c+j)%M] = curr
            apps[curr] = (new_r, new_c, h, w)

    for app_id, direction in commands:
        move(app_id, direction)

    return board

    return board





print(solution(



[[0, 2, 2, 0, 0, 0, 0, 0], [0, 2, 2, 0, 0, 4, 4, 0], [0, 3, 3, 3, 1, 4, 4, 0], [0, 3, 3, 3, 0, 0, 0, 0], [0, 3, 3, 3, 5, 5, 6, 0], [0, 0, 0, 0, 5, 5, 0, 0]], [[3, 1], [3, 1]]))
