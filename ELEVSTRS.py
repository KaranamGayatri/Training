T = int(input())
for i in range(T):
    N,V1,V2 = map(int,input().split())
    Elevator = V1*2**0.5/(N)
    Stairs = V2/N
    if Elevator<Stairs:
        print("Elevator")
    else:
        print("Stairs")