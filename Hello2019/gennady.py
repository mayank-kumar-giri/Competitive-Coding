card = input()
hand = list(input().split())
f=0
for i in hand:
    if i[1]==card[1] or i[0]==card[0]:
        f=1
        print("YES")
        break
if f==0:
    print("NO")