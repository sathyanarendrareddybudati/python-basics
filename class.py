# class Person:
#     def __init__(self,name,age,height):
#         self.name=name
#         self.__age=age
#         self.height=height
#     def student(self):
#         print(self.__age)
#     def man(self):
#         self.student()
# obj=Person("sat",1,6)
# # print(obj.name)
# # print("my age is {}".format(obj.age))
# obj.man()


class hello:
    def run(self):
        for i in range(5):
            print("hello")
class hii:
    def run(self):
        for i in range(5):
            print("hii")
t1=hello()
t2=hii()

t2.run()
t1.run()