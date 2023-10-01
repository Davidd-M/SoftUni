num_seq = input().split()
message = list(input())
decrypted_list = []
for seq in num_seq:
    index = 0
    for char in seq:
        index += int(char)
    index %= len(message)
    decrypted_list.append(message[index])
    message.pop(index)
print("". join(decrypted_list))
