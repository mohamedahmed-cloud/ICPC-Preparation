def isPalindrome(n):
 
    # `rev` stores reverse of a binary representation of `n`
    rev = 1
 
    # do till all bits of `n` are processed
    k = n
    while k > 0:
        # add the rightmost bit to `rev`
        rev = (rev << 1) | (k & 1)
        k = k >> 1          
        print(k,rev)
    return n == rev
 
 
if __name__ == '__main__':
 
    n = int(input())    # 1001
 
    if isPalindrome(n):
        print(f'{n} is a palindrome')
    else:
        print(f'{n} is not a palindrome')