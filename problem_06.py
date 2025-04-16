# Greatest of two numbers:
num1=int(input("enter a first number:"))
num2=int(input("enter a second number:"))
if (num1 > num2):
    print("{} and {} = {} is greater".format(num1,num2,num1))
elif(num2 > num1):
    print("{} and {} = {} is greater".format(num1,num2,num2))
else:
    print("{} and {} both are equal".format(num1,num2))