for i in range(int(input())):
    n = int(input())
    d = input().split()
    print(d)
    m = sum(map(int, d)) % n
    print(m*(n-m))
