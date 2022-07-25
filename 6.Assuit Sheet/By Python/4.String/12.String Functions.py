import sys
sn,sl=map(int,sys.stdin.readline().split())
string=sys.stdin.readline()
for i in range(sl):
    take=sys.stdin.readline().split()
    if take[0]=="pop_back":
        string=string[0:len(string)-2]
    elif take[0]=="front":
        print(string[0])
    elif take[0]=="back":
        print(string[-1])
        # print(string)
    elif take[0]=="substr":
        print(string[int(take[1])-1:int(take[2])])
    elif take[0]=="print":
        print(string[int(take[1])-1])
    elif take[0]=="push_back":
        string=string+take[1]
        # print(string)
    elif take[0]=="reverse":
        out=[]
        out =list(string[int(take[1])-1:int(take[2])])
        out.reverse()
        string=string[:int(take[1])-1] + "".join(out) +  string[int(take[2]):]
        # print(string)
    elif take[0]=="sort":
        out=[]
        out =list(string[int(take[1])-1:int(take[2])])
        out.sort()
        string=string[:int(take[1])-1] + "".join(out) +  string[int(take[2]):]