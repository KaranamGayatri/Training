import math

def minimize_travel_time(T, test_cases):
    results = []
    for case in test_cases:
        N, V1, V2 = case
        time_elevator = 2 * N / V2
        time_stairs = N * math.sqrt(2) / V1
        if time_elevator < time_stairs:
            results.append("Elevator")
        else:
            results.append("Stairs")
    return results

T = 3
test_cases = [(5, 10, 15), (2, 10, 14), (7, 14, 10)]
print(minimize_travel_time(T, test_cases))