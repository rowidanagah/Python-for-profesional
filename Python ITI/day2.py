
lst =[1,2,3,4,3]
lst2 =[1,4,3]

#lst.extend(lst2)
lst.append(lst2)

print(lst2, lst)
print(lst.__len__())
print(lst.__len__)

lst.remove(3)
print(lst)

print("iti" in lst)


arr = ['dana', 'iti', 'jk12']

arr.sort()

arr[::-1]
#print(lst.index("iti"))

X = ['Rowida' , 'Dana' ]
x = dict(zip([i+1 for i in range(2)] , X))
t1 = (2,3,4)
t2 = ("k", 'm', 'l')
print(x)
#print(dict(zip[t2,t1]))
print(dict((X, [1,2])))

tmp = dict([X, [1,2]])
print(tmp)
for k,v in tmp.items():
    print(k,v)



XX = set(["ali", "da", "a"])

print(XX)


def longest_substr(str):
    n, max_sub_len = len(str), 0
    for i in range(n):
        for j in range(i,n):
            if ''.join(sorted(str[i:j])) == str[i:j]:
               print(''.join(sorted(str[j:i])), str[j:i])
               max_sub_len = (max_sub_len, i-j+1)
        print("-----------")
    return max_sub_len

def tmp(str):

    n, max_sub_len = len(str), 0
    for i in range(n):
        for j in range(i,n):
            print(i, j)
            if ''.join(sorted(str[i: j+1])) == str[i: j+1] :
                max_sub_len = max(max_sub_len,j-i+1 )
    return  max_sub_len

print(tmp('abdulrahman'))