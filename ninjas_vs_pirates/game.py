from classes.ninja import Ninja
from classes.pirate import Pirate
import time



jack_sparrow = Pirate("Jack Sparrow")

def game_over():
        for i in range(5):
            time.sleep(1) 
            i = print("GAME OVER!") 
        return i

while(True):

    name = input(f"Your name: ")
    player = Ninja(name)
    print(f"Hello {player.name}! You are promoted to Ninja! Congratulations")
    time.sleep(2)
    print("Watch out, Jack Sparrow is attacking you!  ")
    time.sleep(2)
    print("What do you want to do next?")
    time.sleep(2)
    print(f"You have {player.health} Health and {player.strength} Strength")
    print("Let's attack Jack Sparrow!")
    time.sleep(2)
    player.attack(jack_sparrow)
    print("Your attack was precise, let's prepare for the counter attack")
    time.sleep(5)
    jack_sparrow.attack(player)
    print("OHHH NOOO!!! Jack Sparrow attacked you, let's check your status... ")
    time.sleep(3)
    print(f"Your Health is {player.health} and Jack Sparrow's Health is {jack_sparrow.health}")
    time.sleep(1)
    print(f"Jack Sparrow's damage is {jack_sparrow.strength} and your damage is {player.strength}")
    time.sleep(5)
    print("You're right, we won't be able to win the fight against Jack Sparrow, let's run away!")
    time.sleep(7)
    game_over()
    choice = input(f"Wanna play again {player.name}? ")
    if choice != "yes" and choice != "y":
        print("OK, Good Bye!")
        break
    