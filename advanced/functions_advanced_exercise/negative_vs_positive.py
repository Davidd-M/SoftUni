def neg_or_pos(iter_list):
    neg_sum = 0
    pos_sum = 0
    for num in iter_list:
        if int(num) < 0:
            neg_sum += int(num)
        else:
            pos_sum += int(num)
    print(neg_sum)
    print(pos_sum)
    if abs(neg_sum) > pos_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")
    return


ls = [int(x) for x in input().split()]
neg_or_pos(ls)
