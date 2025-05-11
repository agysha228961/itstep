print("hi world")

class Pet:
    def __init__(self,name,typee,sound):
        self.name = name
        self.typee = typee
        self.sound = sound
    def play_sound(self):
        print(f"{self.typee} по имине {self.name} говорит{self.sound}")
class human:
    def __init__(self,name,age,pets = None,):
        self.name = name
        self.age = age
        self.pets = []
        
    def getpet(self,pet):
        if not isinstance(pet,Pet):
            print(f"нельзя взять питомца:{pet}")
            return
        else:
            print(f"{self.name} получил {pet}")
            self.pets.append(pet)
    def playpet(self):
        if self.pets:
            print(f"{self.name}игрет с пет:")
            for pet in self.pet:
                pet.play_sound()
        else:
            print(f"{self.name}нет питомца")


mura = Pet("mura","kot","may")
bob = human("bob",21)
bob.playpet()
bob.getpet(mura)
bob.playpet()

