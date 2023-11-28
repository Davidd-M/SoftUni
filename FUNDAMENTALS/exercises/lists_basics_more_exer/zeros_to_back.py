inp_str = input().split(", ")

counter = 0

while "0" in inp_str:
    inp_str.remove("0")
    counter += 1
for zero in range(counter):
    inp_str.append("0")
int_list = [int(x) for x in inp_str]
print(int_list)