a = int(input())
b = int(a/2)
i = 1

while i <= a and b >= 0 : 
    

    print(b*" "+i*"*"+(b)*" "+(b)*" "+i*"*"+(b)*" ")
    
    b -= 1
    i += 2
    if i == a : 
        break
    
while i >= 1 and b >= 0: 
        print(b*" "+i*"*"+(b)*" "+(b)*" "+i*"*"+b*" ")
        b += 1
        i -= 2


