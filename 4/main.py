lst = ['asd','asf','asd','ldg','asfd','asf']
dct ={lst[i]:lst.count(lst[i]) for i in range(len(lst))}
print(*[dct[i] for i in dct])
