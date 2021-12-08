class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk( self ):
        self.pet.play()
        return self
    def feed( self ):
        self.pet.eat()
        print(f'You fed your Pet: {self.pet.name}')
        return self
    def bathe(self):
        print(f'You bathe your Pet: {self.pet.name}, they seem excited! {self.pet.noise()}')

#     # implement the following methods:
#     # walk() - walks the ninja's pet invoking the pet play() method
#     # feed() - feeds the ninja's pet invoking the pet eat() method
#     # bathe() - cleans the ninja's pet invoking the pet noise() method

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    def play(self ):
        self.health += 5
        self.energy -= 15
        print(f'You and your dog went walking, your pets vitality increase to: H-{self.health}|E-{self.energy}')
        return self
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def noise(self):
        print('Woof! Woof!')
        return self
    
#     # implement __init__( name , type , tricks ):
#     # implement the following methods:
#     # sleep() - increases the pets energy by 25
#     # eat() - increases the pet's energy by 5 & health by 10
#     # play() - increases the pet's health by 5
#     # noise() - prints out the pet's sound


dog = Pet("billy","dog","backflip")
ninja = Ninja("John", "Junior", "bacon", "kibble", dog).walk().walk().feed().bathe()

