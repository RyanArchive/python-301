class Animal:
    fur_color = "White"

    def speak(self):
        raise NotImplementedError

    def jump(self):
        pass

    def run(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Meow")

cat = Cat()
cat.speak()