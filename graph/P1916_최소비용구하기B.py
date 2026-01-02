import heapq
import sys 
input = sys.stdin.readline 
INF = sys.maxsize

# n: 도시의 개수(노드), m: 버스의 개수(간선)를 입력받습니다.
N = int(input())
M = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만듭니다.
# 인덱스 번호를 노드 번호와 맞추기 위해 (n + 1) 크기로 생성합니다.
graph = [[] for _ in range(N+1)]

# 모든 간선 정보를 입력받습니다.
for _ in range(M):
    u, v, w = map(int, input().split())   # u에서 v로 가는 비용 w
    graph[u].append((v, w))               # u번 노드에서 v번 노드로 가는 비용이 w라는 의미
    
# 시작 노드와 도착 노드 번호를 입력받습니다.
start_city, end_city = map(int, input().split())

# 최단 거리 테이블을 모두 무한(INF)으로 초기화합니다.
distance = [INF]*(N+1)

def dijkstra(start, end):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입합니다.
    # (거리, 노드) 순서로 넣어야 거리순으로 정렬됩니다.
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:    # 큐가 비어있지 않다면 반복
        dist, now = heapq.heappop(q)   # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기

        # 조기 종료 
        # 힙에서 꺼낸 노드가 end_city라면, 그 시점의 비용이 무조건 최솟값이므로 즉시 종료하고 값을 반환
        if now == end:
            return dist
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시합니다.
        # (기록된 거리보다 큐에서 꺼낸 거리가 더 크다면 이미 더 짧은 경로를 찾은 것)
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인합니다.
        for next_node, weight in graph[now]:
            cost = dist + weight      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리를 계산

            # 현재 노드를 거쳐서 이동하는 거리가 더 짧은 경우 거리 테이블을 갱신합니다.
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return distance[end]

print(dijkstra(start_city, end_city))