'''
You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines, which
will follow. On the following n lines, you will receive liters of water (integers), which you should pour into your tank.
If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last
line, print the liters in the tank.
'''
capacity_litres = 255
number_lines = int(input())
received_litre = 0
current_litres = 0
for litre in range(number_lines):
    received_litre = int(input())
    if received_litre + current_litres > capacity_litres:
        print("Insufficient capacity!")
    else:
        current_litres += received_litre
print(f'{current_litres}')