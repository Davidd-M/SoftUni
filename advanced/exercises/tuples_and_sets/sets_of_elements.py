n, m = input().split()
n, m = int(n), int(m)
n_set = set()
m_set = set()

for line in range(n):
    n_set.add(input())
for line in range(m):
    m_set.add(input())

print('\n'.join(n_set.intersection(m_set)))
