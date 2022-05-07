for _ in range(int(input())):
    l, r, a = map(int, input().split())
    d = max((r//a)*a-1, l)
    # print(int(r/a)*a-1)
    print(d)
    print(max((r//a)+(r%a), (d//a)+(d%a)))