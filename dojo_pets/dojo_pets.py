from ninja import Ninja 
from pets import Pet  


# doggy1 = Pet("Doggy", "dog", ["sit","roll", "bark"],"wuff wuff")
# owner1 = Ninja("Jack", "Farmer", "meat balls", "dry balls", doggy1)

pet1 = Pet("Doggy", Pet.pet_type[0], Pet.tricks[:], Pet.noise[0])
pet2 = Pet("Catty", Pet.pet_type[1], Pet.tricks[0], Pet.noise[1])
owner1 = Ninja("Jack", "Bauer", Ninja.treats[0], Ninja.pet_food[1], pet1)
owner2 = Ninja("Jacky", "Bauer", Ninja.treats[2], Ninja.pet_food[2], pet2)

print(owner1.walk().feed().bathe())
print()
print(owner2.walk().feed().bathe())
