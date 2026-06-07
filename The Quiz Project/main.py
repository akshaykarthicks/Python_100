class User:

    def __init__(self,userid,username):
        self.id=userid
        self.name=username
user_1=User("001","AK")
user_2=User("002","aAK")

print(user_1.id)
print(user_1.name)