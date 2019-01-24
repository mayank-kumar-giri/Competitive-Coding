t = int(input())
for i in range(t):
    s = input()
    arr = list(s.split(' '))
    if "not" in arr:
        print("Real Fancy")
    else:
        print("regularly fancy")