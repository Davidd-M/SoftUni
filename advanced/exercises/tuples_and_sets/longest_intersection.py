n = int(input())
longest_intersection = set()

for _ in range(n):
    first, second = input().split("-")
    first_start, first_end = first.split(",")
    second_start, second_end = second.split(",")
    first_range = set(el for el in range(int(first_start), int(first_end)+1))
    second_range = set(el for el in range(int(second_start), int(second_end)+1))
    if len(first_range.intersection(second_range)) > len(longest_intersection):
        longest_intersection = first_range.intersection(second_range)

longest_intersection = sorted(longest_intersection)
print(f"Longest intersection is [{', '.join([str(el) for el in longest_intersection])}] with length {len(longest_intersection)}")
