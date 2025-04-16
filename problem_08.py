# Leap year or not
number=int(input("enter a number:"))
if(number%4==0 and number%100!=0 or number%400==0):
  print("leap year")
else:
    print("not leap year")
