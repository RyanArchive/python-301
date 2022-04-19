class MyClass:
    names = ["Billy", "Chas", "Robin", "Vince"]

    def add_name(self, name):
        self.names.append(name)
        return self.names

    def get_names(self):
        print(self.names)
    
    @property
    def get_second(self):
        return self.names[1]

my_class = MyClass()

my_class.get_names()

name = my_class.get_second
print(name)

my_class.add_name("Beth")
my_class.get_names()