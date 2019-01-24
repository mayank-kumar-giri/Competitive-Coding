vot = []
nfhd = {-5:[213,232],-2:[123,1232],-7:[12,1232],1:[123,12],6:[324,123,1232]}
sd = list(sorted(nfhd.items()))
print(sd)
for i in sd:
    vot+=i[1]
print(nfhd)
print(vot)