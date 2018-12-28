import re
import itertools as it

print(bin(369)[2:].zfill(10),bin(55))
# ['0', '1', '0', '1', '1', '1', '0', '0', '0', '1']
def perm(s):
    l = re.split('\B',s)
    return set(list(it.permutations(l,len(l))))
temp_perms = perm(bin(35)[2:].zfill(7))
perms = []
for j in temp_perms:
    temp = ""
    for l in j:
        temp += l
    dec_temp = int(temp, 2)
    if dec_temp <= (89) and dec_temp >= 1:
        perms.append(temp)
        print(temp,int(temp,2),bin(90-int(temp,2)))
# print(int("",2))