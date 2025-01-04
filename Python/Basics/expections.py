import sys
try:
    x=int(input("x:"))
    y=int(input("y:"))
    result= x/y
except ValueError:
    print("Invalid input")
    sys.exit(1)
except ZeroDivisionError:
    print("Division zero isnt allowed")
    sys.exit(1)
else :
    print(f"{x} divided by {y} is {result}")

