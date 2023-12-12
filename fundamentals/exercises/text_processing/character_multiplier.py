'''
Create a program that receives two strings on a single line separated by a single space. Then, it prints the sum of
their multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum,
then continue with the next two characters. If one of the strings is longer than the other, add the remaining
character codes to the total sum without multiplication.
'''

str1, str2 = input().split()
result = 0

if len(str1) > len(str2):
    try:
        for i in range(len(str1)):
            result += ord(str2[i]) * ord(str1[i])
    except IndexError:
        for j in str1[i::]:
            result += ord(j)
elif len(str2) > len(str1):
    try:
        for i in range(len(str2)):
            result += ord(str1[i]) * ord(str2[i])
    except IndexError:
        for j in str2[i::]:
            result += ord(j)
else:
    for i in range(len(str1)):
        result += ord(str1[i]) * ord(str2[i])

print(result)
