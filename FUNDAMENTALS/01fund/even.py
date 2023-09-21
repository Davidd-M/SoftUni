nums = int(input())
num = 0
for _ in range(nums):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        quit()
print("All numbers are even.")


