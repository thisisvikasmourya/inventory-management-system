# Making or Creating a class
class Email:

    # Initialising a function
    def __init__(self):
        self.is_sent = False

    # Initialising a function
    def send_email(self):
        self.is_sent = True

# Calling a above function
my_email = Email()
print(my_email.is_sent)
my_email.send_email()
print(my_email.is_sent)
