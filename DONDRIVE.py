T = int(input())

for i in range(T):
    N,X = map(int, input().split())
    
    difference = N - X
    print(max(0 ,difference))