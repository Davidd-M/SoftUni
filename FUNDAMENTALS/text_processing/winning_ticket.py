tickets = input().split(", ")
winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    ticket = ticket.strip()
    winning_ticket = False
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    for index in range(10, 5, -1):
        if not winning_ticket:
            for winning_symbol in winning_symbols:
                if winning_symbol * index in ticket[0:10] and winning_symbol * index in ticket[10:20]:
                    winning_ticket = True
                    if index == 10:  # jackpot
                        print(f'ticket "{ticket}" - {index}{winning_symbol} Jackpot!')
                    else:
                        print(f'ticket "{ticket}" - {index}{winning_symbol}')
                    break

    if not winning_ticket:
        print(f"ticket \"{ticket}\" - no match")
