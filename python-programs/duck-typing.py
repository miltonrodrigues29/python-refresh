x = 5
x = "Navin"

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Executing")


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Executing")

class Laptop:
    def code(self,ide):
        ide.execute()


ide = MyEditor()
a = Laptop()
a.code(ide)  #it does not matter which class object you are passing, matter is, that class object should have that method
