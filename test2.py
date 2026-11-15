def solution(h, grid, panels, seqs):
    from collections import deque, defaultdict
    import heapq
    
    n = len(grid) // h
    m = len(grid[0])
    
    g = []
    elev = None
    for f in range(h):
        floor = []
        for r in range(n):
            row = grid[f * n + r]
            floor.append(row)
            for c in range(m):
                if row[c] == '@':
                    elev = (f + 1, r + 1, c + 1)
        g.append(floor)
    
    k = len(panels)
    p_pos = {}
    for i, (f, r, c) in enumerate(panels):
        p_pos[i + 1] = (f, r, c)
    
    pre = defaultdict(set)
    for a, b in seqs:
        pre[b].add(a)
    
    def bfs(start_f, start_r, start_c):
        dist = {}
        q = deque([(start_f, start_r, start_c, 0)])
        dist[(start_f, start_r, start_c)] = 0
        
        while q:
            f, r, c, d = q.popleft()
            
            if d > dist.get((f, r, c), float('inf')):
                continue
            
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 < nr <= n and 0 < nc <= m and g[f-1][nr-1][nc-1] != '#':
                    nd = d + 1
                    if nd < dist.get((f, nr, nc), float('inf')):
                        dist[(f, nr, nc)] = nd
                        q.append((f, nr, nc, nd))
            
            if g[f-1][r-1][c-1] == '@':
                for nf in range(1, h):
                    if nf != f:
                        nd = d + abs(nf - f)
                        if nd < dist.get((nf, r, c), float('inf')):
                            dist[(nf, r, c)] = nd
                            q.append((nf, r, c, nd))
        
        return dist
    
    all_dist = {}
    for pid in range(1, k + 1):
        all_dist[pid] = bfs(p_pos[pid])
    
    start = p_pos[1]
    all_dist[0] = bfs(*start)
    
    pq = [(0, 0, frozenset())]
    best = {}
    
    while pq:
        time, last, active = heapq.heappop(pq)
        
        state = (last, active)
        if state in best and best[state] <= time:
            continue
        best[state] = time
        
        if len(active) == k:
            return time
        
        for nxt in range(1, k + 1):
            if nxt in active:
                continue
            
            if not pre[nxt].issubset(active):
                continue
            
            pos = p_pos[nxt]
            
            if last == 0:
                d = all_dist[0].get(pos, float('inf'))
            else:
                d = all_dist[last].get(pos, float('inf'))
            
            if d == float('inf'):
                continue
            
            new_time = time + d
            new_active = active | frozenset([nxt])
            new_state = (nxt, new_active)
            
            if new_state not in best or best[new_state] > new_time:
                heapq.heappush(pq, (new_time, nxt, new_active))
    
    return -1

# Test cases
print(solution(3, [".#.##..", ".#..##.", ".......", "##.###.", ".@.#...", "...#..."],
                           [[2, 3, 4], [2, 5, 6], [1, 1, 1], [3, 6, 3]],
                           [[3, 2], [1, 2], [4, 1], [4, 3]]))  # Expected: 36