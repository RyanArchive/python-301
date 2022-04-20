class Animal:
    fur_color = "White"

    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Meow")

class Lion(Animal):
    fur_color = "Orange"

    def speak(self):
        print("Rawr")

cat = Cat()
print("Cat")
print(cat.fur_color)
cat.speak()

tiger = Lion()
print("\nLion")
print(tiger.fur_color)
tiger.speak()