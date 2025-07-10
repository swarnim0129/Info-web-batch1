#For loop While loop
#range(start, stop-1, step)
#1 2 3 4 5 6 7 8 9 10
# for i in range(2,11,1):
#     print(i)

# name = "Python"
# for i in name:
#     print(i)

# fruits = ["apple", "banana", "cherry"]
# print(fruits)   
# for i in fruits:
#     print(i)

# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#     print(i+3)

# for i in range(11,1,-1):
#     print(i)

# #While loop
# i=10
# while i > 1:
#     print(i)
#     i -= 1

# name = "Python"
# i = 0
# while i < len(name):
#     print(name[i])
#     i += 1

# fruits = ["apple", "banana", "cherry"]
# i=0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# numbers = [1, 2, 3, 4, 5]
# i = 0
# while i < len(numbers):
#     print(numbers[i] + 3)
#     i += 1

# i=1
# while i <=10:
#     print(i)
#     i+=2

#-----------------------------------------------------------------------------------------
# passwrod="admin123"
# attempts = 0

# while attempts < 3:
#     entered_password = input("Enter your password: ")
#     if entered_password == passwrod:
#         print("Access granted")
#         break
#     else:
#         attempts += 1
#         print(f"Incorrect password. You have {3 - attempts} attempts left.")
# if attempts == 3:
#     print("Access denied. Too many incorrect attempts.")

#-----------------------------------------------------------------------------------------------
# fruits=["banana","bpple","cherry"]

# print(fruits[0])

# for f in fruits:
#     print(f)

# fruits.append("litchie")
# print(fruits)

# # fruits.remove("banana")
# # print(fruits)

# fruits.insert(3,"orange")
# print(fruits)

# fruits.pop()
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits)

# nums=[10,2,3,5,6]
# nums.sort(reverse=True)
# print(nums)

# fruits.clear()
# print(fruits)

#-----------------------------------------------------

#dictionaries

# student={
#     'name':"Rahul",
#     'age':20,
#     'city':"Mumbai",
# }

# # print(type(student))
# # for key in student:
# #     print(key , student[key])

# # for key , value in student.items():
# #     print(f"{key} => {value}")

# student["email"]="xyz@gmail.com"
# print(student)

# student.update({'phone':123456})
# print(student)

# student.update({'name':"Ram"})
# print(student)


# student.pop('age')
# print(student)

# print(student.keys())
# print(student.values())


#----------------------------------------------------
#Tuples

# a=(1,2,3,4,5,5,3,5,5)
# # print(a[2])

# b=(1)
# print(type(b))

# # for i in a:
# #     print(i)

# print(a.count(5))
# print(a.index(5))

# print(a)

# a[0]=100
# print(a)

#------------------------------------------------------
# Sets

colors={"red","yellow","purple",0.1,0.2,3,4,5,6,7,8,"green"}
floats={0.1,0.2,0.3,0.4}
print(colors)


# colors.add("yellow")
# print(colors)

# colors.remove("green")
# print(colors.remove("green"))

# colors.discard("yellow")
# # print(colors.discard("yellow"))

# # print(colors[0])
# colors.pop()



# lists=[]
# tuples=()
# sets={}
# dictionaries={'key':'value'}

print(colors.union(floats))
print(colors.intersection(floats))

# print(colors.difference(floats))
a={1,2,3}
b={3,4,5}
print(b.difference(a))