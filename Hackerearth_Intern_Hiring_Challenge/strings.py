t = int(input())
for i in range(t):
    a = input()
    b = input()

    minimum = 3000

    flag = 0

    for a_iter in range(len(a)-1):
        if a[a_iter]==b[0]:

            if len(b)==1:
                minimum = 0
                flag = 1
                break

            b_index = 1

            for iter in range(a_iter+1,len(a)):
                if b_index==(len(b)-1) and a[iter]==b[b_index]:
                    flag = 1
                    curr_length = ((iter-a_iter)+1)-len(b)

                    if minimum>=curr_length:
                        minimum=curr_length
                    break
                elif a[iter]==b[b_index]:
                    b_index += 1

    if flag == 0:
        print("No")
    else:
        print("Yes")
        print(minimum)