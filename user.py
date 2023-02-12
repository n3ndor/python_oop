class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points


def display_info(self):
    print(f"First Name: {self.first_name}")
    print(f"Last Name: {self.last_name}")
    print(f"Email: {self.email}")
    print(f"Your Age: {self.age}")
    print(f"Your Reward Status: {self.is_rewards_member}")
    print(f"Your Gold Card Points: {self.gold_card_points}")


# This user is active member, with points
user1 = User("Nandor", "Nagy", "nandor.nagy@aol.com", 33, True, 300)
# This user is not a member, no points
user2 = User("John", "Doe", "johnydondy@email.com", 21)
# This user is active member, with no points
user3 = User("Maria", "Schmidt", "marias@mail.de", 41, True)
# This user is not anymore active, with points
user4 = User("Viky", "Pool", "myviky@nofake.com", 18, False, 200)


def enroll(self):
    if self.is_rewards_member == False:  # preventing from re-enrolling if already a member
        self.is_rewards_member = True
        self.gold_card_points = self.gold_card_points + 200
    else:
        print("Errors:")
        print(f"User {self.first_name} already a member.")
# enroll(user2)
# # display_info(user2)


def spend_points(self, amount):
    if self.gold_card_points == 0:
        print(f"User {self.first_name} don't have enough Points left to spend")
    else:
        self.gold_card_points = self.gold_card_points - amount


spend_points(user1, 50)
enroll(user2)
spend_points(user2, 80)

display_info(user1)
print("")  # using empty print to see the user in a separate block
display_info(user2)
print("")
display_info(user3)
print("")
display_info(user4)

enroll(user1)
spend_points(user3, 40)
