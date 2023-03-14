import math

print("welcom to your calculator :)")

print("menu: ")
print("+: sum")
print("-: sub")
print("*: multiplication")
print("/: division")
print("sin")
print("cos")
print("tan")
print("cot")
print("log")
print("factorial")
print("sqrt")

print("please choose your operator: ")

op = input()

if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("enter your first number"))
    b = float(input("enter your first number"))
else:
    a = float(input("enter your number"))

if op == "+" :
     result = a + b
elif op == "-" :
    result = a - b
elif op == "*" :
    result = a * b
elif op == "/" :
    if b == 0 :
        print("Dividion by zero is invalid :)")
    else: 
        result = a / b
elif op == "sin" :
    c = a * math.pi / 180
    d = math.sin(c)
    result = (d)
elif op == "cos" :
   c = a * math.pi / 180 
   d = math.cos(c)
   result = (d)
elif op == "tan" :
    c = a * math.pi / 180 
    d = math.tan(c)
    result = (d)
elif op == "cot" :
    c = a * math.pi / 180 
    d = math.tan(c)
    e = 1 / d
    result = (e)
elif op == "log" :
    result = math.log(a)
elif op == "factorial" :
    result = math.factorial(a)
elif op == "sqrt" :
    result = math.sqrt(a)

print("your result is: ", result)