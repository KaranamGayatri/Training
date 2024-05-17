t = int(input())
for i in range(0,t):
    x,y = map(int,input().split())
    sum = x+y
    
    if sum > 6:
        print("Yes")
    else:
        print("No")