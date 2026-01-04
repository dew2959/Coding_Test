from sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)  # 진입차수 배열

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1  # 집입차수 데이터 저장

result = []
q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:  # 위상정렬 수행
    now = q.popleft()
    result.append(now)

    for next in graph[now]:  #해당 노드와 연결된 노드에서 진입차수 빼기 
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

print(*result)
