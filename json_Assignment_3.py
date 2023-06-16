class Dog:
    def __init__(self, name, age, coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color
    
    def description(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')

    def get_info(self):
        print(f'Coat color: {self.coat_color}')
    
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
    
    def bark(self):
        print("Jack Russell Terrier barks loudly!")
    
    def jump(self):
        print("Jack Russell Terrier jumps high!")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
    
    def snore(self):
        print("Bulldog snores loudly!")
    
    def chew(self):
        print("Bulldog loves to chew on things!")


dog1 = Dog("Charly", 5, "Brown")
dog1.description()
dog1.get_info()
print()


jack = JackRussellTerrier("Rusty", 3, "White")
jack.description()
jack.get_info()
jack.bark()
jack.jump()
print()


bulldog = Bulldog("Max", 4, "Fawn")
bulldog.description()
bulldog.get_info()
bulldog.snore()
bulldog.chew()