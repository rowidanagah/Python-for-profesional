## What ’re the methods that you used ?

- weekday

- strptime

- total_seconds

- zip

- eval

## Explain each method ..

- weekday 
    - ***Syntax*** : `calendar.weekday(year, month, day)`.
    - ***Parameters*** : **year** year number , **month** month number (1–12) and  **day** day (1–31) .
    - ***Returns*** : Returns the number day of the week  .

- strptime 
    - ***Syntax***  : `strptime (str or code format)`
    - ***Parameters*** : **string** (that be converted to datetime) , **code format** .
    - ***Returns*** : Based on the string and format code used, the method returns its equivalent datetime object.

- total_seconds 
    - ***Signature***  : ` total_seconds()`
    - ***Parameters*** : Takes no parameters .
    - ***Returns*** : Returns the duration represented by the timedelta object as number of seconds

- zip 
    - **Signature***  : `zip(*iterators)`
    - ***Parameters*** : Python iterables or containers such as  list, string etc .
    - ***Returns*** : Returns a single iterator object, having mapped values from all the containers.
- eval
    - ***Syntax*** :  `eval(expression, globals=None, locals=None)`.
    - ***Parameters*** : 
        - **expression** : to be parsed and evaluated as a Python expression .
        - **globals**  : (optional): a dictionary to specify the available global methods and variable
        -  **locals** :  (optional): another dictionary to specify the available local methods and variables.
    - ***Returns*** : the result evaluated from the ** expression ** .



## What’s new for you ?
- weekday
- strptime


## Resources ? 
- [python documentation about calender](https://docs.python.org/3/library/calendar.html)
- [tutorial about striptime](https://www.programiz.com/python-programming/datetime/strptime)
- [python documentation about math](https://docs.python.org/3.7/library/math.html)
- [python documentation about float](https://docs.python.org/3/library/functions.html)
- [tutorial about eval](https://www.geeksforgeeks.org/eval-in-python/)
