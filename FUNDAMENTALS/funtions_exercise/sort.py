def list_sorting(ints_list):
    return sorted(ints_list)


inp_list = input().split()
inp_list = [int(x) for x in inp_list]
print(list_sorting(inp_list))
