# Prime number
number=int(input("enter a number:"))
count=0
if number < 2:
    print("not_prime")
else:
    for i in range(1,number+1):
        if number%i==0:
            count+=1
           
    if count==2:
        print("prime")
    else:
        print("not_prime")
            

