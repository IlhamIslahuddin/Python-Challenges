import random

class Character:
    def __init__(self):
        self.name = ""
        self.attack = 0
        self.defence = 0
        self.__health = 0
        self.experience = 0

    def print_basics(self):
        print("\nName: ",self.name)
        print("attack: ",self.attack)
        print("defence ",self.defence)
        print("health: ",self.__health)
        print("experience: ",self.experience)

    def setter(self, name):
        self.name = name
        self.attack = random.randint(0, 50)
        self.defence = random.randint(0, 50)
        self.__health = random.randint(30, 50)

    def health_getter(self):
        return self.__health

    def print_me(self):
        self.print_basics()

class wizard(Character):
    def __init__(self):
        Character.__init__(self)
        self.magic = 30

    def print_me(self):
        self.print_basics()
        print("magic ",self.magic)

class knight(Character):
    def __init__(self):
        Character.__init__(self)
        self.armour = 30

    def print_me(self):
        self.print_basics()
        print("armour ", self.armour)

caste = input("\nWould you like to be a Wizard or Knight? W or K")
char_name = input("And what is your name?")

if caste.upper() == "K":
    print("A great knight is created!")
    you = knight()
elif caste.upper() == "W":
    print("A great wizards shimmers into existance")
    you = wizard()
else:
    print("\nTyping W or K too much for you! \nClearly you plan to die...\nBasic peasant for you!")
    you = Character()
    you.setter(char_name)
    you.print_me()
    print("\nThere's a game to be made here! \nBut the gods of youtube have not delivered me enough subscribers!")
