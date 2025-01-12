class Pet:
    def init(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100
    
    def eat(self):
        self.energy += 20
        print(f"{self.name} поїв! Енергія: {self.energy}")

    def play(self):
        self.energy -= 30
        print(f"{self.name} грається! Енергія: {self.energy}")

    def sleep(self):
        self.energy += 50
        print(f"{self.name} спить! Енергія: {self.energy}")

    def years(self):
        self.energy += 100
        print(f"{self.name} сьогодні йому 2 роки! Енергія: {self.energy}")

    def got_sick(self):
        self.energy -= 200
        print(f"{self.name}  йому погано! Енергія: {self.energy}")

    def check_energy(self):
       if self.energy < 100:
           print("ти програв!")
       else:
           print("у тебе все добре!")
        

my_pet = Pet("Тед", 5)
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.years()
my_pet.check_energy()
