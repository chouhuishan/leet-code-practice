from collections import Counter


def maximum_total_importance_roads(n: int, roads: list[list[int]]) -> int:
    flattened_road_ls = [char for char in roads if char.isdigit()]
    num_counts = Counter(flattened_road_ls)
    # print(num_counts) # Counter({'2': 4, '1': 3, '0': 2, '3': 2, '4': 1})
    degree = list(num_counts.values())
    print(degree)


n = int(input())  # number of cities
roads = input()

print(maximum_total_importance_roads(n, roads))
