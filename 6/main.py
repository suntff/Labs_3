s = "вврпв Аорми ваыравс джджа кт"
s = s.split()
for i in range(len(s)):
    if 1072<=ord(s[i][0])<=1103:
       print(chr(ord(s[i][0])-32)+s[i][1:],end=" ")
    if 1040<=ord(s[i][0])<=1071:
       print(s[i][0]+s[i][1:],end=" ")