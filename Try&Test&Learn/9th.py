s = input()
arr = [input() for  i in range(int(input()))]
w = dict.fromkeys(arr, 0)

for i in arr:
	mat = 0
	tot = 0
	for j in range(len(i)):
		for x in s:
			if i[j] == x:
				mat += 1
				tot += 1
			else:
				tot += 1
	w[i] = round((mat/tot), 2)

lol = dict(sorted(w.items(),key=lambda item:(item[1],item[0])))

for k in reversed(list(lol.keys())):
    fnum=lol[k]
    res = "{:.2f}".format(fnum)
    print(k, res)