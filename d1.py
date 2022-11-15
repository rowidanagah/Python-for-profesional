"""
What is time complexity of following code :

        int count = 0;
        for (int i = N; i > 0; i /= 2) {
            for (int j = 0; j < i; j++) {
                count += 1;
            }
        }
      
ans O(n)

Which of the given options provides the increasing order of complexity of functions f1, f2, f3 and f4:

f1(n) = 2^n

f2(n) = n^(3/2)

f3(n) = nLogn

f4(n) = n^(Logn)

ans f3, f2, f4, f1




In the following C++ function, let n >= m.


int gcd(int n, int m) {
  if (n%m ==0) return m;
  if (n < m) swap(n, m);
  while (m > 0) {
    n = n%m;
    swap(n, m);
  }
  return n;
}
What is the time complexity of the above function assuming n > m?. 
Θ symbol represents theta notation and Ω symbol represents omega notation.

ans log(n)



What is the worst case time complexity of the following code:

int findMinPath(vector<vector<int> > &V, int r, int c) {
  int R = V.size();
  int C = V[0].size();
  if (r >= R || c >= C) return 100000000; // Infinity
  if (r == R - 1 && c == C - 1) return 0;
  return V[r][c] + min(findMinPath(V, r + 1, c), findMinPath(V, r, c + 1));
}
Assume R = V.size() and C = V[0].size().


O(2 ^ (R + C))

---------- 


What is the worst case time complexity of the following code:

int memo[101][101];
int findMinPath(vector<vector<int> >& V, int r, int c) {
  int R = V.size();
  int C = V[0].size();
  if (r >= R || c >= C) return 100000000; // Infinity
  if (r == R - 1 && c == C - 1) return 0;
  if (memo[r][c] != -1) return memo[r][c];
  memo[r][c] =  V[r][c] + min(findMinPath(V, r + 1, c), findMinPath(V, r, c + 1));
  return memo[r][c];
}

Callsite : 
memset(memo, -1, sizeof(memo));
findMinPath(V, 0, 0);
Assume R = V.size() and C = V[0].size() and V has positive elements

NOTE : This question involves recursion which will be explained later in topic Backtracking. So, if you are not able to approach this question now, you can give it a try later.

o(r*c)

"""




class Solution:
	# @param A : list of integers
	# @return an integer
	def countInversions(self, A):
		n = len(A)
		return sum(1 for i in range(n) for j in range(i,n) if A[i] >A[j])
s = Solution()







def merge(arr, left, mid, right):
    i = left
    j = mid
    k = 0
    invCount = 0
    temp = [0 for x in range(right - left + 1)]
 
    while (i < mid) and (j <= right):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
 
        else:
            temp[k] = arr[j]
            invCount += mid - i
            k += 1
            j += 1
 
    while i < mid:
        temp[k] = arr[i]
        k += 1
        i += 1
 
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
 
    k = 0
    for i in range(left, right + 1):
        arr[i] = temp[k]
        k += 1
 
    return invCount
 
 
def mergeSort(arr, left, right):
    invCount = 0
 
    if right > left:
        mid = (right + left) // 2
 
        invCount = mergeSort(arr, left, mid)
        invCount += mergeSort(arr, mid + 1, right)
        invCount += merge(arr, left, mid + 1, right)
 
    return invCount
 
 

class Solution:
	# @param A : list of integers
	# @return an integer
	def countInversions(self, A):    
		return mergeSort(A, 0, len(A) - 1)