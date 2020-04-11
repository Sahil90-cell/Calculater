print("This is a calculater\nPlease enter your first number")
n1 = input()
print("Enter your Secend number")
n3 = input()
print("enter Operater")
n2=input()
if n2 == "+":
    print("your anser is", (int(n1) +int(n3)))
elif n2 =="-":
    print("your anser is", (int(n1) - int(n3)))
elif n2 == "*":
    print("your anser is", (int(n1) *int(n3)))
elif n2== "/":
    print("your anser is", (int(n1) /int(n3)))
elif n2 == "%":
    print("your anser is", (int(n1) % int(n3)))
