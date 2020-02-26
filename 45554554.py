a = input().split()
a1 = int(a[0])
a2 = int(a[1])
s = a2
for i in range(a1):
    t = input().split()
    t1 = int(t[0])
    t2 = int(t[1])
    s = s - t2
if s > 0:
    print(s)
else:
    print(0)