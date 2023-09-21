'''
Everybody knows that you spend too much time awake during nighttime.
Your task is to define how much coffee you need to stay awake. Until you receive the command "END", you need to
read commands on different lines. According to the commands, calculate the number of coffees you need to drink
to stay awake during the daytime.
The list of events can contain the following:
• You have homework to do ("coding").
• You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
• You watch a movie ("movie").
• If other events are present, they will be represented by arbitrary strings. Just ignore them!
Each event can be lowercase or uppercase:
• If it is lowercase, you need 1 coffee by an event.
• If it is uppercase, you need 2 coffees by an event.
In the end, print the number of coffees you will need. If the count has exceeded 5, just print "You need extra
sleep".
'''
coffees = 0
while True:
    if coffees > 5:
        print("You need extra sleep")
        break
    action = input()
    if action == "END":
        print(f'{coffees}')
        break
    elif action == 'coding':
        coffees += 1
    elif action == 'dog' or action == 'cat':
        coffees += 1
    elif action == "movie":
        coffees += 1
    elif action == 'CODING' or action == 'DOG' or action == 'CAT' or action == 'MOVIE':
        coffees +=2
    else:
        continue

