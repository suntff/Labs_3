a = 'baafhasrrrrrddww'
#str(input())
i = 1
c = 1
while i<len(a):
    if a[i] == a[i - 1]:
        c += 1
    else:
        if c != 1:
            a = a[:i-c+1] + str(c) + a[i:]
            i = len(a[:i-c] + str(c))-1
            c = 1
    if i==len(a)-1:
        a = a[:i - c+2] + str(c)
    i+=1
print(a)