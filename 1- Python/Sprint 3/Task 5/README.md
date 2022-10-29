## What ’re the methods that you used ?

- numpy.array()

-  numpy.eye()

- numpy.inner()

- numpy.outer()


## Explain each method ..

-  numpy.array()
    - **Syntax***  : `numpy.reshape(a, newshape, order='C')`
    - ***Parameters*** : **obj** , **newshape** and  **order** .
        - obj : (iter , array_like ) it's the array hat needed to be reshaped
        - newshape : (int, tuple of int ) The new shape should be compatible with the original shape.
        - copy : (bool ,optional) equal to True as default Otherwise, a copy will only be made if __array__ returns a copy.
    - ***Returns*** : Returns ndarray ,This will be a new view object if possible; otherwise, it will be a copy.

-  numpy.eye()
    - **Syntax***  : `numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C')`
    - ***Parameters*** : **N** , **M** and  **K** , **dtype** and **order** .
        - N :(int ) Number of rows in the output.
        - M : (int ,optional) Number of cols in the output ,If None, defaults to N..
        - K : (int ,optional) Index of the diagonal0 as default refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower dig.
        - dtype : (data-type, optional) Data-type of the returned array.
        - order : (‘C’, ‘F’}, optional) 
    - ***Returns*** : Returns ndarray of shape (N,M) ,An array where all elements are equal to zero, except for the k-th diagonal, whose values are equal to one.

- numpy.inner()
    - **Syntax***  : ` numpy.inner(a, b) `.
    - ***Parameters*** : **a**  and **b** .
        - a and b : (array_like) If a and b are nonscalar, their last dimensions must match.
    - ***Returns*** : Returns ndarray , ndarray.shape = a.shape[:-1] + b.shape[:-1]
    - Compute the inner product of two vectors.


- numpy.outer()
    - **Syntax***  : `numpy.outer(a, b, out=None) `.
    - ***Parameters*** : **a** , **b**  and **out**.
        - a and b : (array_like) If a and b are nonscalar, their last dimensions must match.
        - out(M, N) (ndarray, optional)  location where the result is stored .
    - ***Returns*** : Returns **(M, N)ndarray** , out[i, j] = a[i] * b[j]
    - Compute the outer product of two vectors.



## What’s new for you ?
- XML


## Resources ? 

- [numpy documentation about array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
- [numpy documentation about reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)
- [numpy documentation about transpose](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)
- [numpy documentation about flatten](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html)
- [numpy documentation about concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)
- [numpy documentation about std](https://numpy.org/doc/stable/reference/generated/numpy.std.html)
- [numpy documentation about var](https://numpy.org/doc/stable/reference/generated/numpy.var.html)
