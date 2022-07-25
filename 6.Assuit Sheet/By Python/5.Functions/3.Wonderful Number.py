n=int(input())
def odd(n):

    if n%2==1:
      return "YES"
    else:
        return "NO"
def isPalindrome(n):

    rev = 0
    k = n
    while k > 0:
        rev = (rev << 1) | (k & 1)
        k = k >> 1  
    return n == rev
x=odd(n)
y=isPalindrome(n)
if x =="YES" and y :
    print("YES")
else:print("NO")