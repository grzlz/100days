class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        print("New user being created...")

user_1 = User("001", "memo")
print(user_1.username)

user_2 = User("002", "many")
print(user_2.name)