#n * 2 columns
#n rows     and  |

n = int(input())
print("*" * (n * 2) + " " * n + "*" * (n * 2))

for i in range(n - 2):
    if i == (n-1) // 2 - 1:
        print("*" + "/" * ((n - 1) * 2) + "*" + "|" * n + "*" + "/" * ((n - 1) * 2) + "*")
    else:
        print("*" + "/" * ((n - 1) * 2) + "*" + " " * n + "*" + "/" * ((n - 1) * 2) + "*")
print("*" * (n * 2) + " " * n + "*" * (n * 2))

