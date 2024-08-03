class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def welcome(self):
        print(f"Welcome, {self.username}.")

    def check_password(self, password):
        return self.password == password

    def __str__(self):
        return f"User(username={self.username})"
from datetime import datetime

class SubscribedUser(User):
    def __init__(self, username, password, expiry_date):
        super().__init__(username, password)
        self.expiry_date = expiry_date

    def is_expired(self):
        return datetime.now() > self.expiry_date

    def __str__(self):
        return f"SubscribedUser(username={self.username}, expiry_date={self.expiry_date})"
user = User(username="john_doe", password="securepassword123")
user.welcome()  
print(user.check_password("securepassword123"))  
print(user.check_password("wrongpassword"))  

expiry_date = datetime(2024, 8, 31)  
sub_user = SubscribedUser(username="jane_doe", password="anotherpassword456", expiry_date=expiry_date)
sub_user.welcome()  
print(sub_user.check_password("anotherpassword456"))  
print(sub_user.is_expired())
