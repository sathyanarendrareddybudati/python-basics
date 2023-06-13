# a=input()
# b=input()
# c=input()
# a=int(a)
# b=int(b)

# if c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c=="*":
#     print(a*b)
# elif c=="/":
#     print(a/b)
# elif c=="%":
#     print(a%b)
# elif c=="//":
#     print(a//b)
# else:
#     print("Enter correct sign-")


# def calculator():
#   print("\n")
#   try:
#     a=float(input("Enter the first number :"))
#     b=float(input("Enter the second number :"))
#   except ValueError as ERROR:
#     print("invalid input\n")
#     print("\ntry again")
#     return
#   c=input("Enter an operation : +-*/  ")
#   if c=="+":
#      ans = (a+b)
#   elif c=="-":
#     ans = (a-b)
#   elif c=="*":
#     ans = (a*b)
#   elif c=="/":
#     try:
#       ans = (a/b)
#     except ZeroDivisionError as ERROR:
#       print("invalid equation\n")
#       print(ERROR)
#       print("\nTry again")
#       return      
#   else:
#     ans="invald operation"
#   print(f"Ans: {ans}")
# while True:
#     calculator()
#     d=input("do you want next calculation? (yes/no) : ")
#     if d == "no":
#         break  
#     else:
#         print("invalid input")


# add a number in a tuple '4'
# a=(1,2,3,4,[1,2,3])
# b=list(a)
# a[4].append(4)
# x=tuple(b)
# print(a)

# print the range between 0 to 31 

# for i in range(0,31):
#   if i % 3 ==0 and i % 5==0:
#     print("fizz")
#   elif i % 3 ==0:
#     print("bizz")
#   elif i % 3 ==0:
#     print("fizzbuzz")
#   else:
#     print(i)

# adding of two dictories
# a={1,2,3}
# b={4,5,6}
# c=("**a,**b")
# print(c)

# c=zip(a,b)
# c=(**a,**b)  
# c=a|b

# a={1,2,3}
# b={4,5,6}
# c=a|b
# print(c)

# adding of two list
# c=a+b
# a.extend(b)


# def satya(a):
#   return a**2
# print(satya(2))

# dulal=[1,2,3,4,5]
# map(satya,dulal)
# list(map(satya,dulal))


# def urooj(a):
#   return a%2==0
# print(urooj(2))

# l=[]
# a=[1,2,3,4,5]
# for i in a:
#     if i % 2==0:
#         # print(i)
#         l.append(i)

# for i in range(0,11):
#     if i ==0:
#         print("True")
#     elif i ==1:
#         print("True")
#     elif i ==2:
#         print("True")
#     elif i ==3:
#         print("True")
#     elif i ==4:
#         print("True")
#     elif i ==5:
#         print("True")
#     else:
#         print("Flase")

# a=int(input())

# for i in a:
#     if i>6:
#         print("True")
#     else:
#         print("False")

# a={"name":"sat","no":65465}

#  we want to get values of dictories....
# x=a["name"]
# x=a.get("name")
# x=a.keys()
# x=a.values()

# we want to update a dictories...
# a["no"]=655656
# x=a.update({"no":677678})

# if "buyu" in a:
#     print("yes")
# else:
#     print("no")


a = {'Jim': 30, 'Pam': 28,}
b = {'Jiu': 3, 'Pa': 38}
c={**a, **b}
d = a | b
d=dict(zip(a,b))
print(c)
print(d)
# person = input('Get age for: ')

# try:
#     print(f'{person} is {ages[person]} years old.')
# except KeyError:
#     print(f"{person}'s age is unknown.")


# a="sat"
# b="reddy"
# c=" ".join([a,b])
# print(c)

# how to count a words in a string...

# a=str(input())
# b=a.split()
# for i in b:
#     print(str(b.count(i))+" "+str(i))


# a={
#     'b':[1,2,3,4],# length
#     'c':(1,2,3,4),#access 2
#     'd':[[1,2,3,4,5],[6,7,8,9,10]],#flating
#     'e':'',#k value to convert to lower
#     'f':{'g':{'h','i','j'}},#h,i,j access
#     'k':'HAPPY NEW YEAR',#
#     'l':('m','n','o','p'),#reverse
#     'q':['happy','new','year'],#convert into single string
#     'r':{}
# }
# # x=a["d"]
# # print(x[0|1])
# x=a["d"]
# y=[]
# for z in x:
#     for w in z:
#         y.append(w)
# print(y)
# # length of b


# print(len(a["b"]))
# print(a["c"][1])
# x=dict(zip([]))
# print(a["f"]["g"])
# print(a["l"][::-1])
# class dog():
#     def __init__(self,bread):
#         self.bread=bread
# a=dog(bread="gffg")
# print(a.bread)


# class circle():
#     def __init__(self,a):
#         self.a=a
    
#     def area(self):
#         return 3.14 * self.a * self.a
        
#     def circumtance(self):
#         return 2 * self.a * self.a

# c=circle(2)
# print(c.area())
# print(c.circumtance())


# class a(circle):
#     def __init(self,c):
#         self.c=c
#     def area(self):
#         return 3.14 * self.a * self.a
# c=a(5)
# print(c.area())

# import timeit
# timeit.timeit('"-",join(str(n) for n in range(100))', number=10000)

# a=[1,2,3,4,5,6,7,8]
# b=list(filter(lambda n:n % 2 == 0,a))
# print(b)

#string format...
# # a=4
# b="my name is satya and age is 8"
# print(b)

# input  a=[[1,2],[2,3],[5,6]]
# output [[1,3],[5,6]] 


# input=[[1,2],[2,3],[5,6]]






# class Car:
#     def __init__(self,name,color,price):
#         self.name=name
#         self.color=color
#         self.price=price
#         print("gfsf")
#     def information(self):
#         return (self.name,self.color,self.price) 
# n=Car("audi","red",656)
# b=Car("benzz","white",23)
# print(n.information())

# class circle:
#     def __init__(self,a):
#         self.a=a
#     def area(self):
#         return 3.14 * self.a * self.a
# class rectangle(circle):
#     def __init__(self,b,c):
#         self.b=b
#         self.c=c
#     def area(self):
#         return self.b * self.c


class Laptop:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    def special(self):
        return f"{self.name} {self.model}"

a=Laptop("audi",'jjhb',23245)
print(a.special)

