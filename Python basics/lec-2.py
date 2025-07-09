# x=0

# if x>0:
#     print("x is positive")
# elif x == 0:
#     print("x is zero")
# else:
#     print("x is negative")

# x=10
# y=-20

# if x>0:
#     if y>0:
#         print("Both x and y are positive")

#AND&& OR|| NOT
# """x=7
# y=10
# if x>0 and y<15:
#     print("x is positive and y is less than 15")

# if x<0 or y>15:
#     print("Either x is negative or y is greater than 15")

# if not x<0:
#     print("x is not negative")""

#Functions
# name="Jaimeen"
# def greet(name):
#     """This function greets the person passed in as a parameter."""
#     return("Hello, " + name + "!")
# print(greet(name))


# def add(a,b):
#     return a+b

# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b

# def divide(a,b):
#     if b == 0:
#         return "Cannot divide by zero"
#     else:
#         return round(a / b,2)


# #/ //-Quotient %-Remainder
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print("Addition:", add(a, b))
# print("Subtraction:", subtract(a, b))
# print("Multiplication:", multiply(a, b))
# print("Division:", divide(a, b))

def average(a,b,c):
    average= (a + b + c) / 3
    def get_grade(average):
        if average >= 90:
            return "A"
        elif average >= 75 and average < 90:
            return "B"
        elif average >= 60 and average < 75:
            return "C"
        else:
            return "D"
    return get_grade(average)

a=int(input("Enter first marks: "))
b=int(input("Enter second marks: "))
c=int(input("Enter third marks: "))

average_marks = average(a, b, c)

print("Grade:", average_marks)