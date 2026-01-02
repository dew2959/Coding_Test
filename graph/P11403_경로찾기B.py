import sys 
# 빠른 입력을 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

# N: 정점의 개수를 입력받습니다.
N = int(input())

# 그래프의 인접 행렬 정보를 입력받습니다. 
# graph[i][j]가 1이면 i에서 j로 가는 간선이 있다는 뜻이고, 0이면 없다는 뜻입니다.
graph = [list(map(int, input().split())) for _ in range(N)]

# --- 플로이드-워셜 알고리즘을 응용한 경로 탐색 ---
# k: 거쳐가는 중간 노드
for k in range(N):
    # i: 출발 노드
    for i in range(N):
        # j: 도착 노드
        for j in range(N):
            # 만약 i에서 k로 갈 수 있고(1), 동시에 k에서 j로 갈 수 있다면(1)
            # i에서 j로 가는 경로가 존재한다고 판단하여 1을 저장합니다.
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
                
# 결과 출력: 수정된 인접 행렬을 한 줄씩 출력합니다.
# *row는 리스트의 요소를 공백으로 구분하여 출력해주는 문법입니다.
for row in graph:
    print(*row)