"""
Write a function that accepts two arguments (length, start) to
generate an array of a specific length filled with integer numbers
increased by one from start.
"""

def make_arr(length, start):
    arr = [i+start for i in range(length)]
    lst = list(range(start, start+length+1))
    return arr, lst


print("------------------------ q1------------------")
print(make_arr(4, 2))

"""
write a function that takes a number as an argument and if the
number divisible by 3 return "Fizz" and if it is divisible by 5 return
"buzz" and if is is divisible by both return "FizzBuzz"
● Write a function which has an input of a string from use
"""


def FizzBuzz(num):
    if not num % 3 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "buzz"
    return "out of range"


print()
print("------------------------------q2 -----------------")
print(FizzBuzz(15))
print(FizzBuzz(5))
print(FizzBuzz(3))
print(FizzBuzz(22))

"""
Write a function which has an input of a string from user then it
will return the same string reversed.
"""

def rev_str(str):
    return str[::-1]

print()
print("------------------------------q3 -----------------")
print(rev_str("dana"))

"""
Ask the user for his name then confirm that he has entered his
name(not an empty string/integers). then proceed to ask him for
his email and print all this data (Bonus) check if it is a valid email
or not
"""
def validate_email():
    import re
    email = input("your email address : ")
    expr = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(expr, email):
        print("not a valid emaill addres")
        email = validate_email()
    return email

def get_user_name():
    name = input("input your username : ")
    if any(chr.isdigit() for chr in  name) or not name:
        print(" not a valid user name ")
        name = get_user_name()
    return name


def validate_user_info():
    name = get_user_name()
    email = validate_email()
    
    return f"your name if {name} and here is {email}"


print()
print("------------------------------ q4 -----------------")
print(validate_user_info())

"""
Write a function that takes a string and prints the
longest alphabetical ordered substring occurred For example, if
the string is 'abdulrahman' then the output is: Longest substring in
alphabetical order is: abdu
""" """
def q6():
    return 
print()
print("------------------------------ q5 -----------------")
"""

"""
write a program which repeatedly reads numbers until the user
enters “done”.
    ○ Once “done” is entered, print out the total, count, and
    average of the numbers.
    ○ If the user enters anything other than a number, detect their
    mistake, print an error message and ski
"""
def keepOn_reading():
    cnt, summ, input_txt = 0, 0, ''
    while input_txt != "done":
        input_txt = input(" running till done :)' ")

        if any(char.isalpha() for char in input_txt):
            print("error -> chr is not allowed")
            continue
        cnt += 1
        summ += int(input_txt)

    return f"your number or trying is : {cnt} and thier avrg is {summ / cnt} "


print()
print("------------------------------ q5 -----------------")
print(keepOn_reading())

print()
print("------------------------------ q5 -----------------")


def  longest_substr(str):
    n, max_sub_len, res = len(str), 0, ''
    for i in range(n):
        for j in range(i,n):
            if ''.join(sorted(str[i: j+1])) == str[i: j+1] :
                #ab abc
                res = str[i: j+1]  if max_sub_len < j-i+1 else res
                max_sub_len = max(max_sub_len,j-i+1 )

    return res

print(longest_substr("abdulrahman"))