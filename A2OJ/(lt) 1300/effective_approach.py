n = int(input())
arr = list(map(int, input().split()))
q = int(input())
queries = list(map(int, input().split()))

done = [[-1,-1]]*(n+1)
j=0
for i in arr:
    done[i] = [(j+1),(n-j)]
    j+=1

sscore = 0
rscore = 0

for i in queries:
    sscore += done[i][0]
    rscore += done[i][1]
print(sscore,rscore)