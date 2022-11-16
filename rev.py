x,y,z,n = 1,1,2,3

print([(i,j,k) for i in range(x+1) for j in range(y+1)
 for k in range(z+1) if (i+j+k) !=n])


dic = {"Gfg" : 5, "is" : 5, "Best" : 2, "for" : 9, "geeks" : 8}
  

grads = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

print(sorted(grads, key = lambda x :(x[-1], x[0])))


print("Sort by keys",{k:v for k,v in sorted(dic.items(), key= lambda x:x[0])})

print("Sort by Values",{k:v for k,v in sorted(dic.items(), key= lambda x:x[-1])})

print("Sort by Values, and then by keys",{k:v for k,v in sorted(dic.items(), key= lambda x:(x[-1], x[0]))})


import datetime
users = [	
			{'name':'John Cena', 'birthday': datetime.date(1992, 9, 12),
				'size': {'height': 175,'weight': 100}},
			{'name': 'Chuck Norris', 'birthday': datetime.date(1990, 8, 28),
			     'size' : {'height': 180, 'weight': 90}},

			{'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6), 'size': {'height': 185,
			'weight': 110}}
		]

print(sorted(users, key= lambda x :(x["name"])))
print(sorted(users, key= lambda x :(x["size"]["height"], x["size"]["weight"])))


x = 'apple'
print(''.join([i if i in 'aioue' else "" for i in x]))


print(''.join([2*(i if i in 'aioue' else "") for i in x]))


print("Count number of vowel nums",sum(1 for i in x if i in 'aioue'))

print([[(i,j) for i in range(5)] for j in range(5,10)])

from itertools import groupby

c = groupby(['goat', 'dog', 'cow', 1, 1, 2, 3, 11, 10, ('persons', 'man', 'woman')])

ist_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'), \
 'wombat', 'mongoose', 'malloo', 'camel']

sortd_c = groupby(ist_things, key = lambda x : x[0])
print(c)
#print({k: list(v) for k,v in c})

#print({k: list(v) for k,v in sortd_c})

res = {k: list(v) for k,v in sortd_c}

print("resss" , [res[i] for i in res])
print("resss" , [i for i in res])


x = lambda : list(input().split())
lst = [list(x()) for i in range(int(input()))]

"""if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = sum(student_marks[input()])
    print('{0:.2f}'.format(query_name /3))
"""
print(hash((1,2)))