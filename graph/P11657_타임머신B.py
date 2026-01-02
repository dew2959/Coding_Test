import sys 
input = sys.stdin.readline
INF = sys.maxsize                 # 출발점에서 도달할 수 없는 경우 사용할 무한대 값을 설정
n, m = map(int, input().split())  # n: 정점(도시)의 개수, m: 간선(버스 노선)의 개수
edges = []                        # 모든 간선 정보를 담을 리스트                            
dist = [INF]*(n+1)                # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))       # a번 노드에서 b번 노드로 가는 비용 c
    
def bellman_ford(start): 
    dist[start] = 0               # 시작 노드까지의 거리는 0으로 설정

    # 총 n번의 라운드(반복)를 수행합니다.
    # n-1번까지는 최단 거리를 확정하기 위함이고, 마지막 n번째는 음수 사이클 확인용입니다.
    for i in range(n):
        # 매 반복마다 '모든 간선'을 하나씩 확인합니다.
        for j in range(m):
            cur_node, next_node, cost = edges[j]

            # 1. dist[cur_node] != INF: 현재 노드가 시작점에서 도달 가능한 노드인지 확인합니다.
            # 2. 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신합니다.
            if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + cost:
                dist[next_node] = dist[cur_node] + cost

                # n번째 라운드(i == n-1)에서도 값이 갱신된다면 음수 사이클이 존재하는 것입니다.
                if i == n-1:
                    return True    # 음수 사이클 발견!
    return False    # 음수 사이클 없음

# 1번 노드(시작점)를 기준으로 알고리즘을 실행
negative_cycle = bellman_ford(1)
if negative_cycle:  
    # 음수 사이클이 존재하면 최단 거리를 구할 수 없으므로 -1을 출력
    print(-1)
else:
    # 2번 노드부터 n번 노드까지의 최단 거리를 출력
    for i in range(2, n+1):
        if dist[i] == INF:
            # 도달할 수 없는 노드인 경우 -1을 출력
            print(-1)
        else:
            print(dist[i])