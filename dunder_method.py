class Animal:
    fur_color = "White"
    animal = ""

    def __init__(self, fur_color):
        self.fur_color = fur_color

    def get_fur_color(self):
        print(f"Fur Color: {self.fur_color}")

class Cat(Animal):
    def __init__(self, fur_color):
        self.animal = "Cat"
        print(f"Animal: {self.animal}")
        super().__init__(fur_color)

cat = Cat("Orange")
cat.get_fur_color()