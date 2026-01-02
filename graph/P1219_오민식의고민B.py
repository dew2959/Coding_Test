import sys 
from collections import deque
input = sys.stdin.readline 

# N: 도시 수, S: 시작 도시, E: 도착 도시, M: 교통 수단 수
N, S, E, M = map(int, input().split())

edges = []
for _ in range(M):
    u, v, c = map(int, input().split())
    edges.append((u, v, c))

# 각 도시에서 벌 수 있는 돈의 액수
earn = list(map(int, input().split()))

INF = sys.maxsize 
#dist[i]는 i번 도시에 도착했을 때 가질 수 있는 최대 돈 
#아직 못 가는 곳은 -INF로 초기화
dist = [-INF] * N  

#시작하자마자 S도시에 도착하므로 dist[S]를 초기화 
dist[S] = earn[S]

#Bellman-Ford N-1회 반복 
for _ in range(N-1):
    for u, v, c in edges:
        # 시작점에서 도달 가능하고, (현재 돈 + 다음 도시 수입 - 교통비)가 기존보다 크다면 갱신
        if dist[u] != -INF and dist[v] < dist[u] + earn[v] - c:
            dist[v] = dist[u] + earn[v] - c

# 양수 사이클(돈을 무한히 벌 수 있는 구간) 확인
# N번째 반복에서도 값이 커진다면 해당 노드는 양수 사이클에 포함되거나 영향을 받는 노드입니다.
cycle = [False] * N 
for u, v, c in edges:
    if dist[u] != -INF and dist[v] < dist[u] + earn[v] - c:
        # 이 조건이 참이라면 v는 돈을 무한히 벌 수 있는 사이클의 일부입니다.
        cycle[v] = True 

# BFS를 사용하여 '양수 사이클'에서 '도착 도시 E'로 갈 수 있는지 확인
# 단순히 사이클이 있다고 "Gee"가 아니라, 그 사이클을 거쳐 도착지에 갈 수 있어야 합니다.
q = deque()
visited = [False] * N 
for i in range(N):
    if cycle[i]:
        q.append(i)
        visited[i] = True 
while q:
    cur = q.popleft()
    for u, v, c in edges:
        # 현재 사이클 영향권 노드(u)에서 갈 수 있는 다음 노드(v)가 있다면 탐색 대상에 추가
        if u == cur and not visited[v]:
            visited[v] = True 
            q.append(v)
            
if dist[E] == -INF:     # 도착 도시에 아예 갈 수 없는 경우
    print("gg")
elif visited[E]:        # 도착 도시에 갈 수 있는데, 도중에 돈을 무한히 벌 수 있는 사이클을 지날 수 있는 경우
    print("Gee")
else:
    print(dist[E])      # 무한히 벌 수는 없지만 최대로 벌 수 있는 액수 출력
    