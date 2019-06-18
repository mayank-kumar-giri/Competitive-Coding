fp = open("data.txt","r+")
s = ""
for i in fp:
    s += i
fin = ""
ans = ""

for i in range(1,len(s)):
    if s[i-1].islower() and s[i].isupper() and s[i+1].isupper() and s[i+2].isupper() and s[i+3].islower() and s[i+4].isupper() and s[i+5].isupper() and s[i+6].isupper() and s[i+7].islower():
        ans = s[i:i+7]
        fin += s[i+3]
print(fin)


# fp = open("data.txt","r+")
# s = ""
# for i in fp:
#     s += i
# uni = set()
# from collections import Counter
# dd = Counter(s)
# ans = ""
# for i in s:
#     if dd[i]==1:
#         ans += i
#     uni.add(i)
# print(uni)
#
# print(dd)
# print(ans)
# # eaitluqy
# # tequyila