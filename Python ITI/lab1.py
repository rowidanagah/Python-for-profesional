"""
Write a program that counts up the number of vowels 
[a, e, i, o, u]contained in the string
"""

lorem_text = "Lorem Ipsum is simply dummy text of the printing and typesetting \
    industry iti . Lorem Ipsum has been the industry's standard dummy text ever since \
        the 1500s, when an unknown printer took a galley of type and scrambled it  \
to make a type specimen book of iti . It has survived not only five centuries"

print()
print("--------------Q1---------------------")
print(f"number of occerance of volws is : {sum([1 for i in lorem_text if i in 'aiouy'])}")

"""
        Q2 
Fill an array of 5 elements from the user,
 Sort it in descending andascending orders then display the output.
"""
print()
print("--------------Q2---------------------")
arr = [input(f"enter your {i+1} val in arr : ") for i in range(5)]
arr.sort()
print(f"ur sorted arr is : {arr}")
print(f"reverse sortof arr {arr[::-1]} ")


"""
 Q3
 Write a program that prints the number of 
 times the string 'iti' occurs in anystring.
"""
print()
print("---------------------Q3------------------------")
print(f" number of occerance of iti is {lorem_text.count('iti')}")


"""
    Q4
Write a program that remove all vowels from the input word
 and generate a brief version of it.
"""
print()
print("---------------------Q4------------------------")

name = "dana"
print('ur name without vowels', end=" ")
print(''.join([i for i in name if i not in 'oiuyaAIOUY'])) ## dn

"""
    Q5
Writea program that prints the locations of
 "i" character  in any string you added.
"""
print()
print("---------------------Q5------------------------")

lst_of_indexs = [i for i in range(len(lorem_text)) if lorem_text[i] == 'i']
print(* lst_of_indexs)
print( )
print(f"list on indexs of occerance of 'i' chr is : {lst_of_indexs}")


"""
    Q6
Write a program that generate a multiplication
 table from 1 to the number passed
"""
print("--------------Q6------------ ")

num = int(input("limit number of ur multiplication table :  "))

multiplication_table = [[y*i for y in range(1,i+1)] for i in range(1,num+1)]
print(* multiplication_table)

"""
Q7
Write a program that build a Mario pyramid like below:
"""
print("--------------Q7------------ ")
# for i in range(int(input("limit number of ur '*' lines ")),0 , -1 ):
#     print("*" * i)

num_of_lines = int(input("limit number of ur '*' lines "))

for i in range(num_of_lines+1):
     print(" " * (num_of_lines - i) + "*" * (i + 1))
