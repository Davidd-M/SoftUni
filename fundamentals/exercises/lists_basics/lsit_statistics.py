n = int(input())
negatives = []
positive = []
for num in range(n):
    ints = int(input())
    if ints > 0 :
        positive.append(ints)
    elif ints < 0:
        negatives.append(ints)
count_positives = len(positive)
sum_of_negatives = sum(negatives)
print(positive)
print(negatives)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
