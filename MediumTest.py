#prime number 1 to num
num=int(input('Enter last number : '))
for i in range(1,num):
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
            break
    if count==0 and i!=1:
        print(i,end=' ')