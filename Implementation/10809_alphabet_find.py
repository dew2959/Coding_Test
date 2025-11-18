import sys 
input = sys.stdin.readline
S = input().strip()
result = [S.find(chr(i)) for i in range(97,123)]
print(*result)