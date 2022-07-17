# problem Name : Alphabet Rangoli
# Problem Link : https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import string
alphabet=string.ascii_lowercase
# print(alphabet)
size=int(input())
arr=[]
for i  in range(size):
    s="-".join(alphabet[i:size])
    arr.append((s[::-1]+s[1:]).center(size*4-3,"-"))
print("\n".join(arr[:0:-1]+arr))
