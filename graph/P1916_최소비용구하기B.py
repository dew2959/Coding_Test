import heapq
import sys 
input = sys.stdin.readline 
INF = sys.maxsize

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
start_city, end_city = map(int, input().split())
distance = [INF]*(N+1)

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if now == end:
            return dist
        if distance[now] < dist:
            continue
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return distance[end]

print(dijkstra(start_city, end_city))