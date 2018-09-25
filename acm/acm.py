import statistics as st
for it in range(int(input())):
    n,sd = map(int,input().split())
    sd=float(sd)
    f=0
    while f!=1:
        arr=sample(range(1,),n)
        if st.stddev(arr)==sd:
            f=1
    print(arr)