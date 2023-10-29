class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_list = []
command = input()
while command != "Stop":
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails_list.append(email)
    command = input()

indices = input().split(', ')
for index in indices:
    emails_list[int(index)].send()
for email in emails_list:
    print(email.get_info())
