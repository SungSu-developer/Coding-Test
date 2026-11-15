from collections import defaultdict, deque

def solution(city, road):
    n = len(city)
    nodes = {}  # 좌표 -> 노드 id
    edges = defaultdict(list)
    node_id = 0
    
    # 도시 노드
    for i, (x, y) in enumerate(city):
        nodes[(x, y)] = node_id
        node_id += 1
    
    # 도로 중앙점 추가
    cameras = {}
    for x1, y1, x2, y2, limit in road:
        cx, cy = (x1+x2)/2, (y1+y2)/2
        if (cx, cy) not in nodes:
            nodes[(cx, cy)] = node_id
            node_id += 1
        # 카메라 제한
        if (cx, cy) in cameras:
            cameras[(cx, cy)] = min(cameras[(cx, cy)], limit)
        else:
            cameras[(cx, cy)] = limit
        
        # 도시/노드와 연결
        for pt in [(x1, y1), (x2, y2)]:
            if pt not in nodes:
                nodes[pt] = node_id
                node_id += 1
            edges[nodes[(cx, cy)]].append((nodes[pt], limit))
            edges[nodes[pt]].append((nodes[(cx, cy)], limit))
    
    # Dijkstra-like 최대 최소 제한 속도 계산
    import heapq
    start = nodes[tuple(city[0])]
    max_speed = [0]*node_id
    visited = [False]*node_id
    heap = [(-float('inf'), start)]  # 우선순위: -최소속도 (최대 최소)
    
    while heap:
        cur_speed, u = heapq.heappop(heap)
        cur_speed = -cur_speed
        if visited[u]:
            continue
        visited[u] = True
        max_speed[u] = cur_speed
        for v, limit in edges[u]:
            if not visited[v]:
                next_speed = min(cur_speed, limit) if cur_speed != float('inf') else limit
                heapq.heappush(heap, (-next_speed, v))
    
    # 도시별 결과
    res = []
    for i in range(1, n):
        node = nodes[tuple(city[i])]
        speed = max_speed[node]
        if speed == float('inf'):
            res.append(0)
        else:
            res.append(speed)
    return res



print(solution(
[[-1, 3], [7, 3], [1, -1], [-2, 6]], [[-1, 7, 7, 7, 80], [-3, 3, 9, 3, 45], [-2, -4, -2, 6, 60], [1, -4, 1, 8, 50], [5, 1, 5, 7, 70]]))