import os 
dir_path = os.path.dirname(os.path.realpath('__file__'))
print(dir_path)

for  root , foldr, file in os.walk(dir_path):
	print(len(foldr) , root.split('\\')[-1] ,file)



with open('test_ch30.txt' , 'w+') as file:
	##print('Blew the lid of ur life' , file) ## that won't add this line inthe folder
	file.write('Blew the lid of ur life')
	file.write('Blew the lid of ur life')
	file.write('Blew the lid of ur life \n')#note python won't add a new line by default,so you've to add "\n" at the end if u neew a new line as a break
	file.write('Blew the lid of ur life')


"""
To check if the file exits or not
use `os.path.isfile`
"""

isfile = True if os.path.isfile('test_ch30.txt') else False
print(isfile)


"""
To check if path exits or not
use `os.path.isfile`
"""
path = os.path.exists('../root')
path_ac = os.path.exists('../api')
print(path , path_ac)

print(dir_path)
#print(os.path.join('app' , 'api'))
print(os.getcwd())

print(dir_path)
## os.makedirs('Hola')
try :
	"""
	makedirs would eraise error if we try to make a new existing file,
	yet we can easely handle this eeror user `OSError`
	"""
	os.makedirs('./Hola')
except OSError as error : 
	print('Already broken' , error) 

##os.chdir('Hola')
"""
makedir vs makedirs in python
https://stackoverflow.com/questions/13819496/what-is-different-between-makedirs-and-mkdir-of-os
"""
dir_path = os.path.dirname(os.path.realpath('__file__'))
print(dir_path)

