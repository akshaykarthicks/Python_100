class User:

    def __init__(self,userid,username):
        self.id=userid
        self.name=username
        self.followers=0
        self.following=0 
    
    def follow(self,user):
        user.followers+=1    
        self.following+=1




user_1=User("001","AK")
user_2=User("002","aAK")

user_1.follow(user_2) #user 1 follow user 2 
user_2.follow(user_1)


print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
