T = int(input())

for i in range(T):
    N,M = map(int, input().split())
    
    max_pepole_can_travel = N*5 + M*7
    print(max_pepole_can_travel)