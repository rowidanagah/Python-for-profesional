## What is a Context Manager?

 It's an object, that is notified when a context starts and ends, of a class that implements the 2 magic methods `__enter__` and `__exit__` and any other methods if needed. 

  
  __For example__: when a context manager ends, the object file is closed. 
  
```python
with open('test_ch30.txt' , 'w+') as file:
	file.write('Blew the lid of ur life')
  
 # the open file has automaticlly been clossed 
```

  Context manager is commonly used with reading and writing files to assist in conserving system memory and improve resource management by ensuring that each process holds its resources while executing.

  > Opening a file using `with` statement ensures that [File descriptor](https://www.computerhope.com/jargon/f/file-descriptor.htm) are closed automatically.



## How  `with` statment implements a context manager?

  1-  When an object is called with a `with` statment, the 
   interpreter invokes the `__eneter__` method ,which is used to 
   call and performe the setup code required and needed for the 
   process yo be excuted, before the `with` statment.

  2- 	When the `with` statments ends, the interpreter invokes the `__exit__` method .



*Illustartion* :


![alt text][logo]

[logo]: https://i.pinimg.com/originals/4d/58/99/4d589946718af5d2bc4c7f19a6221960.jpg "context_excution_circle"



## What's required to implement a contect manager class?

```python
class ContextManager(object):
	"""docstring for ContextManager"""
	def __init__(self):
		pass
		
	def __enter__(self):
		print("__enter__()")
		# optionaly return an obj
		return "an instance"

	def __exit__(self , exc_type , exc_val , traceback):
		print("__exit__ with " , exc_val if exc_val else ' nope')


with ContextManager() as e:
	print("is a " , e)

```

##  Multiple context managers
```python

with open('test_ch30.txt') as input_file, open('test_ch77.txt', 'w') as output_file:
	# do something with both files.
	# e.g. copy the contents of input_file into output_file
	for line in input_file:
		output_file.write(line + '\n')

# It has the same effect as nesting context managers:
with open('test_ch30.txt') as input_file:
	with open('test_ch77.txt', 'w') as output_file:
		for line in input_file:
			output_file.write(line + '\n')

```


## Manage Resources

```python 
class File():
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
	def __enter__(self):
		self.open_file = open(self.filename, self.mode)
		return self.open_file
	def __exit__(self, *args):
		self.open_file.close()


for _ in range(10000):
	with File('test_ch30.txt', 'w') as f:
		f.write('foo')

```

## ManageFile class follow. 

ManageFile class follow/adhere the context manager protocole and support the with statment [Code link](https://github.com/Rowida46/Python-for-profesional/blob/main/Playing_with_Folders/Context_Manager.py#L16)