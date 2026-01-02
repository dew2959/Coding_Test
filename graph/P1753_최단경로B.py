import heapq
import sys 
input = sys.stdin.readline
INF = sys.maxsize

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())
# 시작 정점의 번호를 입력받습니다.
start_k = int(input())

# 각 노드에 연결되어 있는 노드 정보를 담는 리스트(인접 리스트) 생성
graph = [[] for _ in range(V+1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(V+1)

# 모든 간선 정보를 입력받아 그래프에 저장
for _ in range(E):
    u, v, w = map(int, input().split())   # u 정점에서 v 정점으로 가는 가중치가 w라는 의미
    graph[u].append((v, w))
    
def dijkstra(start):
    q = []
    # 시작 노드 정보를 우선순위 큐에 삽입 (거리 0, 노드 번호)
    # heapq는 튜플의 첫 번째 원소(거리)를 기준으로 정렬합니다.
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 가장 짧은 거리에 있는 노드 정보를 꺼냅니다.
        dist, now = heapq.heappop(q)

        # 현재 꺼낸 거리(dist)가 이미 저장된 최단 거리(distance[now])보다 크다면
        # 이미 방문하여 처리된 적이 있는 노드이므로 무시합니다. (중요 최적화)
        if distance[now] < dist:
            continue

        # 현재 노드(now)와 연결된 인접 노드들을 하나씩 확인
        for next_node, weight in graph[now]:
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리를 계산
            cost = dist + weight

            # 계산된 거리가 기존에 저장된 최단 거리보다 짧은 경우에만 갱신
            if cost < distance[next_node]:
                distance[next_node] = cost

                # 갱신된 노드 정보를 우선순위 큐에 삽입
                heapq.heappush(q, (cost, next_node))
                
dijkstra(start_k)

# 1번 정점부터 V번 정점까지의 최단 거리를 차례대로 출력
for i in range(1, V+1):
    if distance[i] == INF:
        # 경로가 없는 경우 "INF" 출력
        print("INF")
    else:
        # 경로가 있는 경우 최단 거리 값 출력
        print(distance[i])