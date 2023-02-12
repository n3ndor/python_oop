class Pet:
    pet_type = ["dog", "cat", "horse", "fish"]
    tricks = ["sit", "roll", "loud bark", "wait for commando"]
    noise = ["wuff wuff", "miau miau", "boaff boaff"]

    def __init__(self, name , type , tricks, noise):
        self.name = name
        self.pet_type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 10
        self.noise = noise

    def __repr__(self):
        pet = f"{self.name}, pet type: {self.pet_type}, pet can do: {self.tricks}, \n Hey {self.name}, whats your status!? {self.noise} !!!,\n I have {self.health} health and {self.energy} energy"
        return pet

    def sleep(self):
        self.health += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noises(self):
        self.energy -= 10
        self.health += 10
        return self
