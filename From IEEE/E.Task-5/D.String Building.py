# Link of problem is
# "https://codeforces.com/problemset/problem/1671/A"
# -------------
# input operation 
test=int(input())
# Variable
suma=0
sumb=0
# sumacheck="YES"
# sumbcheck="YES"
for k in range(test):
    sumacheck="YES"
    sumbcheck="YES"
    string=input()
    stringa=string.split("b")
    stringb=string.split("a")
    while "" in stringa:
        stringa.remove("")
    while "" in stringb:
        stringb.remove("")
    # output operation 
    for i in range(len(stringa)):
        suma=len(stringa[i])
        if suma>=2 :
            sumacheck="YES"
        elif suma<2 :
            sumacheck="NO"
            break
            
    for i in range(len(stringb)):
        sumb=len(stringb[i])
        if sumb>=2 :
            sumbcheck="YES"
        elif sumb<2 :
            sumbcheck="NO"
            break
    if sumacheck=="YES" and sumbcheck=="YES":
        print("YES")
    else:print("NO")