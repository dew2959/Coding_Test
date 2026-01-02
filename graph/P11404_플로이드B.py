import sys 
# 빠른 입력을 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

# n: 도시의 개수, m: 버스의 개수
n = int(input())
m = int(input())

# 최단 거리 테이블을 무한대(INF)로 초기화합니다.
# 인덱스를 도시 번호와 맞추기 위해 (n+1) x (n+1) 크기로 만듭니다.
INF = int(1e9)
dist = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화합니다.
for i in range(1, n+1):
    dist[i][i] = 0
    
# 간선 정보를 입력받습니다.
for _ in range(m):
    a, b, c = map(int, input().split()) # a에서 b로 가는 비용 c
    # ★ 중요: 시작 도시와 도착 도시를 연결하는 노선이 여러 개일 수 있습니다.
    # 그중 가장 작은 비용만 테이블에 저장합니다.
    dist[a][b] = min(dist[a][b], c)
    
# --- 플로이드-워셜 알고리즘 핵심 로직 (3중 for문) ---
# k: 거쳐가는 도시
for k in range(1, n+1):
    # i: 출발 도시
    for i in range(1, n+1):
        # j: 도착 도시
        for j in range(1, n+1):
            # i에서 j로 바로 가는 것보다 k를 거쳐서 가는 것이 더 빠르다면 갱신합니다.
            # 식: dist[i][j] = min(현재값, i→k 비용 + k→j 비용)
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            
# 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        # 문제 조건: 만약 i에서 j로 갈 수 없는 경우 0을 출력합니다.
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            # 갈 수 있는 경우 최단 거리를 출력합니다.
            print(dist[i][j], end=' ')
    # 한 줄(출발 도시 i 기준) 출력이 끝나면 줄바꿈을 합니다.
    print()