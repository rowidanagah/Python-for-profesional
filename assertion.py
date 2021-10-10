def applay_discount(product , discount):
	price = product['price'] * (1.0 - discount)
	assert 0 <= price <= product['price']
	return price


car = {
	"name" : "catty" ,
	'price' : 100
}

print(applay_discount(car , .2))


"""

Assert : Is a debugging aid and not an run-time error handling.

The proper use of assertion is to tell the developer the
 uncoverable errors in programm 

Use the assertion to  declare the impossible conditions.

if your code is a bug-free, no essertion will be called.

if they do occur,  the programm will crash 
 with an assertion telling u what is the impossiple condition
 was triggered in ur code

"""

assert(1==2 , "Hola")
