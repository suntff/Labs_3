in_str = str(input())+' '
out_str = ''
c = 1

for i in range(len(in_str)):
    if i > 0:
        if in_str[i] == in_str[i - 1]:
            c += 1
        else:
            if c != 1:
                out_str += in_str[i - c] + str(c)
                c = 1
            else:
                out_str += in_str[i - 1]

print(out_str)
