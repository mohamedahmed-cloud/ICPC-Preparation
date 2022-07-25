Key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
Original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
n=int(input())
s=input()
if n==1:
    for i in s:
        index=Original.index(i)
        print(Key[index],end="")

if n==2:
    for i in s:
        index=Key.index(i)
        print(Original[index],end="")