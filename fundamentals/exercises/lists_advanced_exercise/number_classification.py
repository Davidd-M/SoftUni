input_list = input().split(", ")

even_list = [x for x in input_list if int(x) % 2 == 0]
odd_list = [x for x in input_list if int(x) % 2 != 0]
negative_list = [x for x in input_list if int(x) < 0]
positive_list = [x for x in input_list if int(x) >= 0]

print(f"Positive: {', '.join(positive_list)}\n"
      f"Negative: {', '.join(negative_list)}\n"
      f"Even: {', '.join(even_list)}\n"
      f"Odd: {', '.join(odd_list)}")
