#Lambda 
# def add(x,y):
#     return x + y
# add = lambda x,y: x+y
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))

# print(add(a,b))

#map,filter
#Map: used to apply a function to all items in an iterable Syntax: map(function, iterable)
# nums = {1, 2, 3, 4, 5}
# doubled_nums = set(map(lambda x: x + 2, nums))
# print("Doubled numbers:", doubled_nums)

#Filter: used to filter items in an iterable based on a condition Syntax: filter(function, iterable)
# nums = {1, 2, 3, 4, 5}
# even = list(filter(lambda x: x % 2 == 0, nums))
# print(even)

# *args, **kwargs

# def add(*numbers):
#     print(sum(numbers))

# add(1,2,3,4,5)

# def profile(**details):
#     for key,value in details.items():
#         print(f"{key} => {value}")

# profile(name="Jaimeen",age=19,place="Mumbai")


def info( age, *hobbies,name, **details):
    print(name,age,hobbies,details)

info( 19,"coding", "reading", "travelling",city="Mumbai", country="India",college="DJSCE")
