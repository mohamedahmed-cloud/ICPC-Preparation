s = input()
n = int(input())
arr = []
for _ in range(n):
	m = input()
	f = 0
	for i in m:
		if i not in s:
			f = 1
			break
	if f!=1:
		arr.append(m)
def perm(arr, s):
	s = sorted(s)
	out = []
	for i in arr:
		if sorted((i)) == s:
			out.append(i)
		else:
			for j in arr:
				if i != j and sorted((i+j)) == s:
					out.append(f"{i} {j}")

	return out


for i in sorted(perm(arr, s)):
	print(i)