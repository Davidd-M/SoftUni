def even_odd_filter(**kwargs):
    if kwargs.get('even'):
        kwargs['even'] = [int(x) for x in kwargs['even'] if int(x) % 2 == 0]
    if kwargs.get("odd"):
        kwargs['odd'] = [int(x) for x in kwargs['odd'] if int(x) % 2 != 0]
    return dict(sorted(kwargs.items(), key=lambda x: (len(x[1])), reverse=True))


print(even_odd_filter(
        odd=[1, 2, 3, 4, 10, 5],
        even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
    ))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
