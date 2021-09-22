
"""
 To ceate a dic
 ----------------------
"""
x_sqr = {i :i**2 for i in range(3)}
print('x_sqr',x_sqr , '\n' , "---------------------")

X = ['Rowida' , 'Dana' , 'Anas']
x = dict(zip([i+1 for i in range(3)] , X))
print('x' , {i : x[i] for i in x if len(x[i]) >3})
print('Sorted x based on items',sorted(x.items()))
srt =  sorted(x.items())
print({i:j for i,j in x.items() if len(j) > 3} ,'\n' , "-------create--------------")


"""
 reverse the key : val in a  dic 
 ----------------------
"""
reverse = {j:i for i,j in x.items()}
print(reverse , '\n' , "--------Reverse-------------")



"""
 To Merge 2 dics
 ----------------------
"""

merge_dic = {i:j for d in [x , x_sqr] for i,j in d.items()}
print(merge_dic ,'\n' , "------Merge---------------" )
from collections import Counter
cnt = Counter('oh shit here we go again')
print(cnt)
print(cnt.values())

S = [1,2]
from itertools import zip_longest
for i,j in zip_longest(S, x_sqr.values() , fillvalue ='Hola'):
    print(i,j)