'''
Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:
'''
int_n = int(input())
for i in range(int_n):
    for j in range(int_n):
        for k in range(int_n):
            print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}')
