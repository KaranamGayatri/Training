T = int(input())

for i in range(T):
    X,Y = map(int, input().split())
    
    if X < Y:
        print("FIRST")
    elif Y < X:
        print("SECOND")
    elif X == Y:
        print("ANY")