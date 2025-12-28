import heapq
import sys 
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
start_k = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                
dijkstra(start_k)
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])