"""
To Read 
	https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr

"""


class Card(object):
	"""docstring for ClassName"""
	def __init__(self, suit, pips):
		self.suit = suit
		self.pips = pips

ace_of_spades = Card('Spades', 1)
four_of_clubs = Card('Clubs', 4)
six_of_hearts = Card('Hearts', 6)
my_hand = [ace_of_spades, four_of_clubs, six_of_hearts]

print(str(ace_of_spades)) 

"""
Y'all gett <__main__.Card object at 0x0141B2D0>

 as you didn't tell it how you wanted Card instances to be converted to strings.
"""
		

class Card:
	"""
	Whenever you tell Python to create a string from a class instance,
	 it will look for a __str__ method on the class, and
		call it
	"""
	special_names = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}

	def __init__(self, suit, pips):
		self.suit = suit
		self.pips = pips
	def __str__(self):
		card_name = Card.special_names.get(self.pips, str(self.pips))
		return "%s of %s" % (card_name, self.suit)
	def __repr__(self):
		"""
		Python doesn't care about __str__ for this purpose.
			Instead, it looks for a different method,
		 	__repr__, and if that's not found, it falls back on the "hexadecimal thing".[2]
		"""
		card_name = Card.special_names.get(self.pips, str(self.pips))
		return "%s of %s (R)" % (card_name, self.suit)


"""
 __str__ and __repr__ are exactly the same, in this class

 __str__ method was called when we passed our Card **instance** to print and 
  the __repr__ method was called when we passed a list of our instances to print.

"""

ace_of_spades = Card('Spades', 1)
four_of_clubs = Card('Clubs', 4)
six_of_hearts = Card('Hearts', 6)
my_hand = [ace_of_spades, four_of_clubs, six_of_hearts]
print(ace_of_spades)
print(my_hand)


class Card:
	"""
	if a class implements the __repr__ method but not the __str__ method, and you pass an instance of
	that class to str() (whether implicitly or explicitly), Python will fallback on your __repr__
	
	unless If you want different representations for when, for example, inside a container, you'll want to implement both
		__repr__ and __str__ methods

	"""
	special_names = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}

	def __init__(self, suit, pips):
		self.suit = suit
		self.pips = pips

	def __repr__(self):
		card_name = Card.special_names.get(self.pips, str(self.pips))
		return "%s of %s (R)" % (card_name, self.suit)

print("Using __repr__ to represent both an instance and a list of our instance ")

ace_of_spades = Card('Spades', 1)
four_of_clubs = Card('Clubs', 4)
six_of_hearts = Card('Hearts', 6)
my_hand = [ace_of_spades, four_of_clubs, six_of_hearts]
print(ace_of_spades)
print(my_hand)