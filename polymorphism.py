"""

to_read :: https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/polymorphism


## Polymorphism with a Function and objects: 

	Polymorphism without inheritance in python is allowed because of the dynamic type of python ducking

"""

class Duck:
	def quack(self):
		print("DUCK")

	def feathers(self):
		print("Duck have black & white")


class Person:
	def quack(self):
		print("This person is tring to immitate a Duck voice or quack")

	def feathers(self):
		print("Trying to get feathers from the Ducks")

	def name(self):
		print("Dana ...!")


## Polymorphism with a Function and objects:
def in_the_forest(obj):
	obj.quack()
	obj.feathers()


duck = Duck()
dana = Person()
in_the_forest(duck)
in_the_forest(dana)