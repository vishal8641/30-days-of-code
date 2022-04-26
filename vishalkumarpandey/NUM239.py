T=int(input())
for _ in range(T):
    L,R = map(int,input().split())
    i=0
    for j in range(L,R+1):
        if (j%10) == 2 or (j%10) == 3 or (j%10) == 9:
            i+=1
    print(i)
