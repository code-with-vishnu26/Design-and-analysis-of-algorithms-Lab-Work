N, D = map(int, input().split())
l1 = []
curse = 0

for i in range(N):
    x = list(map(int, input().split()))
    l1.append(x)
d=0
while l1:
    small = min(x[0] for x in l1)
    lec = [x for x in l1 if x[0] == small] 
    print(lec)
    lect=lec[0]
    count=0
    while D!=0:
        if D>=lect[1]:
            D=D-lect[1]
        else:
            D=D-1
            count=count-1
    if count==0:
        curse=lect[2]
    l1.remove(lect)  
print(curse)
