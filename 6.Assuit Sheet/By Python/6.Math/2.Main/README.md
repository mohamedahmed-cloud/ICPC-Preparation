# important Notes:

## **sum of number formula**

### ***sum of all number From 1 to n***
`n*(n+1)/2`

### ***Sum of even number from 1 to n***
- even => the number of even number from 1 to n
- even => Terms of even number from 1 to n
  
- **The Sum is** `even(even+1)`
  
### ***Sum of Odd number from 1 to n***
- odd => The number of odd number from 1 to n
- odd => Terms of odd number from 1 to n
- ***The Sum is*** `odd(2)`
----
## ***shift right with left on array***
```py
    from collections import deque
    arr=[1,2,3,4,5]
    myarr=deque(arr)
    myarr.rotate(1)
    print(myarr)
```
----
## ***Note***
`0,1 not a prime number`

---
### ***To multiply Array***
- A is the first martix
- B is the second martix
- res is the Result
```py
def solve(A,B,res):
    import numpy as np
    res=np.dot(A,B)
    return res
```
---
### ***Max distinct Number***
***`Description`***

`Find the max sum of distinct number that equal or less than n`

- we can use for loop with arthimatic series but is will give time limit
```py
def solve(n)
    for i in range(1,n):
        if i(i+1)/2<=n:
            pass
        else:
            return i-1
```
`another perfect solution`
- You should solve the equation 
    `i(i+1)/2<=n`
- by Quadratic formula solution is
 ```py
def solve(n)
    return (-1 + math.sqrt(1 + 8 * n)) // 2
 ```




