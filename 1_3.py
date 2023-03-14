input("name: ")
input("family: ")
a = float(input("Enter the first grade: "))
b = float(input("Enter the second grade: "))
c = float(input("Enter the third grade: "))
average = (a + b + c) / 3
if 17 <= average <= 20 :
    print("Your average is: ", average, "It is Great ! ")
elif 12 <= average < 17 :
    print("Your average is: ", average,  "It is Normal")
else: print("You Lose ):", "Your average is: ", average)
