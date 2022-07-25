t=int(input())
for i in range(t):
    string=input()
    if len(string)<3:
        print("Bad")
    elif len(string)==3:
        if string=="010" or string =="101":
            print("Good")
        else:print("No")
    else:
        ans=""
        for i in range(len(string)-3):
            if string[i:i+3]=="010" or string[i:i+3]=="101":
                ans="Good"
                break
            else:
                ans="Bad"
                
        if ans:
            print(ans)
        else:print("Bad")