'''
Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
The input holds two lines: the number of people N and the capacity P of the elevator.
'''
import math
n_people = int(input())
p_capacity = int(input())
courses = math.ceil(n_people / p_capacity)
print(courses)
