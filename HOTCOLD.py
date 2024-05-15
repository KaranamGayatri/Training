def climate(temp):
    if temp > 20:
        return "HOT"
    else:
        return "COLD"

T = int(input())

for i in range(T):
    temp = int(input())
    print(climate(temp))