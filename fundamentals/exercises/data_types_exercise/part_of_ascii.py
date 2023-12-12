    '''
    Write a program that prints part of the ASCII table characters on the console, separated by a single space. On the
    first line of input, you will receive the char index you should start with. On the second line - the index of the last
    character you should print.
    '''
    start_ind = int(input())
    end_ind = int(input())

    for char in range(start_ind, end_ind + 1):
        print(chr(start_ind), end = " ")
        start_ind += 1