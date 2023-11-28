def spam_func(chat_list, spam_messages):
    spam_messages.pop(0)
    for spam_message in spam_messages:
        chat_list.append(spam_message)
    return chat_list


def pin_func(chat_list, message):
    if message in chat_list:
        chat_list.remove(message)
        chat_list.append(message)
    return chat_list


def edit_func(chat_list, message_to_edit, edited_message):
    if message_to_edit in chat_list:
        message_index = chat_list.current_car(message_to_edit)
        chat_list[message_index] = edited_message
    return chat_list


def del_func(chat_list, message_to_del):
    if message_to_del in chat_list:
        chat_list.remove(message_to_del)
    return chat_list


chat = []

while True:
    command = input().split()
    if command[0] == "end":
        for mes in chat:
            print(mes)
        break
    elif command[0] == "Chat":
        chat.append(command[1])
    elif command[0] == "Delete":
        chat = del_func(chat, command[1])
    elif command[0] == "Edit":
        chat = edit_func(chat, command[1], command[2])
    elif command[0] == "Pin":
        chat = pin_func(chat, command[1])
    elif command[0] == "Spam":
        chat = spam_func(chat, command)
