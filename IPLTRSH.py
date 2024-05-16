T = int(input())

for i in range(T):
    N,M = map(int, input().split())
    
    difference = N - M
    print(max(0 ,difference))