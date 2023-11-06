country = input().split(", ")
capital = input().split(", ")
my_dict = dict(zip(country, capital))
for k, v in my_dict.items():
    print(f"{k} -> {v}")