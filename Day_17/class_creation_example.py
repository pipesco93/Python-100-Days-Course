from matplotlib.style import use


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # When I use a default value I don't have to initialise in ()
        self.following = 0

    def follow(self, user): #method
        user.followers += 1
        self.following += 1

#Example 1
#user_1 = User()

# Adding attributes 
#user_1.id = "001"
#user_1.username = "felipe"

#print(user_1.username)
#If  got a lot of objects creating attributes this way may be unefficient
# I coul deffine attributes directly from the clas using def __init__(self): 
# And under i

#example 2
user_1 = User("001", "Felipe")
user_2 = User("002", "Sofia")

user_1.follow(user_2)

print(user_2.followers)