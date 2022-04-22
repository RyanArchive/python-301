class Animal:
    fur_color = "White"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print("I like to it")

    def run(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Meow")

    def eat(self):
        super().eat()
        print("I like to it fish")

cat = Cat()
cat.speak()
cat.eat()