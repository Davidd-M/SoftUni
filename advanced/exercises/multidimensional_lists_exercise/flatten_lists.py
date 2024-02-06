result = [d for d in input().split("|")]

[print(*[d for d in substr.split()], end=" ") for substr in result[::-1] if any(substr.split())]