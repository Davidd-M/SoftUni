def combine_func(item_list, old_item, new_item):
    if old_item in item_list:
        old_item_index = item_list.index(old_item)
        item_list.insert(old_item_index + 1, new_item)
    return item_list


def drop_func(item_list, item):
    if item in item_list:
        item_list.remove(item)
    return item_list


def collect_func(item_list, item):
    if item not in item_list:
        item_list.append(item)
    return item_list


journal_items = input().split(", ")

while True:
    command = input().split(" - ")
    if command[0] == "Craft!":
        print(", ".join(journal_items))
        break
    elif command[0] == 'Collect':
        journal_items = collect_func(journal_items, command[1])
    elif command[0] == 'Drop':
        journal_items = drop_func(journal_items, command[1])
    elif command[0] == 'Combine Items':
        old_item, new_item = command[1].split(':')
        journal_items = combine_func(journal_items, old_item, new_item)
    elif command[0] == 'Renew':
        if command[1] in journal_items:
            journal_items.remove(command[1])
            journal_items.append(command[1])


