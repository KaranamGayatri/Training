X, Y = map(int, input().split())

if X < Y:
    print("OLD")
elif X > Y:
    print("NEW")
else:
    print("SAME")