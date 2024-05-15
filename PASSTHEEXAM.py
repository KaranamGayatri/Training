def score(A, B, C):
    total = A + B + C
    if total >= 100 and A >= 10 and B >= 10 and C >= 10 :
        return "Pass"
    else:
        return "Fail"
        
T = int(input())

for i in range(T):
    A, B, C = map(int, input().split())
    result = score(A, B, C)
    print(result)