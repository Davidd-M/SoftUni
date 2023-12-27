class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    def set_time(self, new_hours, new_minutes, new_seconds):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self):
        if (self.seconds + 1) < Time.max_seconds:
            self.seconds += 1
        else:
            self.seconds = 00
            if (self.minutes + 1) > Time.max_minutes:
                self.minutes = 00
                if (self.hours + 1) < Time.max_hours:
                    self.hours += 1
                else:
                    self.hours = 00
            else:
                self.minutes += 1

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())

