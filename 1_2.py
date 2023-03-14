print("Please enter the size of the sides you want: ")
a = float(input("The first side: "))
b = float(input("The second side: "))
c = float(input("The third side: "))
if a > (b + c) or b > (a + c) or c > (a + b) :
    print("You cant draw this triangle")
else :
    print("There is no problem in drawing this triangle:) ")
    