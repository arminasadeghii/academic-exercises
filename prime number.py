a = int(input())
b = int(input())
for num in range(a,b+1):
    p = 1 
    for i in range(2,int(num/2)+1): 
        if num % i == 0 : 
            p = 0 
            break
    if p == 1 : 
           print(num)