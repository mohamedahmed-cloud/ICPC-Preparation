import sys
n=list(sys.stdin.readline())
def isseven(n):
    for i in n:
        if i =="7":
            return "YES"
    return "NO"
print(isseven(n))