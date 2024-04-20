class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.start_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index == self.number - 1:
            raise StopIteration

        self.start_index += 1
        idx = self.start_index % len(self.sequence)

        return self.sequence[idx]


result = sequence_repeat('abcde', 5)
for item in result:
    print(item, end ='')
