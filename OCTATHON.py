time = int(input())
if time < 3:
    print("Gold")
elif 3 <= time < 6:
    print("Silver")
elif time >= 6:
    print("Bronze")