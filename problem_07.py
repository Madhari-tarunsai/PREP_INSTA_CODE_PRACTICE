# Greatest of the Three numbers
num1=int(input("enter a first number:"))
num2=int(input("enter a second number:"))
num3=int(input("enter a third number:"))
greatest = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
print(greatest)
