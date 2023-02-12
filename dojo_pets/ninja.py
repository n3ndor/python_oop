

class Ninja:
    treats = ["Meat Balls", "Steak", "Pizza"]
    pet_food = ["Dry Balls", "Sausage", "Mouse"]

    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def __repr__(self):
        owner = f"{self.first_name} {self.last_name}, treats: {self.treats}, pet food: {self.pet_food} \n Pet name: {self.pet}"
        return owner

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noises()
        return self

