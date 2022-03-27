import re
def lambdaMap(arr):
    # ans = [list(map(lambda x : x ** 2 if(x >= 0) else None ,lst)) for lst in arr]
    ans = [[x**2 for x in lst if x > 0] for lst in arr]
    return ans


if __name__ == '__main__':
    arr = [[ -1, 1, 2, -2, 6] , [ 3, 4, -5]]
    ans = lambdaMap(arr)
    for lst in ans :
        print(''.join(str(lst)))
    x = [1,2,3]
    print(list(map(lambda x :(x,2) , x)))
    arr1 = [ -1, 1, 2, -2, 6]
    print(arr1[-1:])
    ans = arr1
    ans.append(2)
    print(arr1, ans)
    pattern = r'123'
    string = 'a123ab'
    ans = re.match(pattern, string)
    pattern = '[a-z]+'
    string = '-----2344-Hello--World!'
    srch = re.search(pattern, string)
    pattern = '[a-z]+'
    string = '-----2344-Hello--World!'
    result = re.search(pattern, string)
    print(result.group())
       

