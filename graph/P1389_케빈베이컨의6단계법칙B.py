import sys 
# 빠른 입력을 위해 사용합니다.
input = sys.stdin.readline

# n: 유저의 수, m: 친구 관계의 수
n, m = map(int, input().split())
# 최단 거리 테이블을 무한대(INF)로 초기화합니다. 
# (n+1) x (n+1) 크기로 만들어 인덱스 번호를 유저 번호와 맞춥니다.
INF = sys.maxsize
dist = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 거리는 0으로 설정합니다.
for i in range(1, n+1):
    dist[i][i] = 0

# 친구 관계(간선) 정보를 입력받아 인접 행렬에 저장합니다.
for _ in range(m):
    a, b = map(int, input().split())
    # 친구 관계는 양방향이므로 양쪽 모두 거리를 1로 설정합니다.
    dist[a][b] = 1
    dist[b][a] = 1
    
# --- 플로이드-워셜 알고리즘 핵심 로직 ---
# k: 거쳐가는 노드, i: 출발 노드, j: 도착 노드
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # i에서 j로 바로 가는 것보다 k를 거쳐서 가는 것이 더 빠르다면 갱신합니다.
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            
# 결과를 저장할 변수 초기화
answer = 0
min_sum = INF

# 각 유저(i)별로 케빈 베이컨 수(다른 유저들과의 거리 합)를 계산합니다.
for i in range(1, n+1):
    # dist[i][1:]은 i번 유저에서 1번부터 n번 유저까지의 거리 리스트입니다.
    s = sum(dist[i][1:])
    
    # 현재 유저의 합(s)이 지금까지의 최소 합보다 작다면 정답을 갱신합니다.
    if s < min_sum:
        min_sum = s 
        answer = i
    # 만약 합이 같다면, 번호가 작은 사람이 우선이므로 별도의 처리를 하지 않습니다. 
    # (반복문이 1번부터 n번까지 순차적으로 돌기 때문)
        
# 케빈 베이컨 수가 가장 작은 사람의 번호를 출력합니다.
print(answer)