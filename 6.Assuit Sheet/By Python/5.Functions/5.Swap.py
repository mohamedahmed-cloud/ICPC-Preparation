import sys
def swap(x,y):
    return y ,x

x,y=map(int,sys.stdin.readline().split())
print(*swap(x,y))