#17.3.2026

#class MyDog:
 #   def __init__(self,name,age):
  #      self.name = name
   #     self.age = age

#dog1 = MyDog("Brark", 20)
#dog2 = MyDog("Yehor", 20)
#print(f"My dog {dog1.name} is {dog1.age} years old")
#print(f"My dog {dog2.name} is {dog2.age} years old")

#dog = MyDog()
#dog.name = "Simon"
#dog.birth_year = 2020
#
#print(f"The dog is named {dog.name} and is born in the year {dog.birth_year}")

#class Car:
 #   pets = 0
  #  def __init__(self, brand, color, sound = "beep"):
   #     self.brand = brand
    #    self.color = color
     #   self.sound = sound
      #  pets = 1
    #def noise(self, times):
     #   for i in range(times):
      #      print(self.sound)
       # return

#car1 = Car("Peugeot", "red", "BEEP")
#car2 = Car("G-Class", "Black")
#car3 = Car("Land Cruiser", "Pink", "Rark Rark")
#car1.noise(2)
#car2.noise(3)
#car3.noise(2)

#Exapmple 2

# class Student:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#     def introduction(self,name,age):
#         print(f"Hello, my name is {name}, and i am {age} years old")
#         return

#student.introduction(student.name, student.age)

# student_list = []
# num_students = int(input("How many students do you wish to add: "))
# count = 0
# for i in range(num_students):
#     s_name = str(input("Please enter a students name: "))
#     s_lastname = str(input("Please enter the students last name: "))
#     s_age = int(input("Please enter the students age: "))
#     student = Student(s_name, s_lastname, s_age)
#     student_list[count] = student

# for i in student_list:
#     i.introduction(student.name, student.age)





#18.3.2026
#Associaton
# class Dog:
#     def __init__(self,name,age, sound = "woof woof"):
#         self.name = name
#         self.age = age
#         self.sound = sound
#     def bark(self, times):
#         for i in range(times):
#             print(f"{self.name} says: {self.sound}")
#         return
#
# class Hotel:
#     def __init__(self):
#         self.dogs = []
#     def checkinn(self, dog):
#         self.dogs.append(dog)
#         print(f"{dog.name} checked inn")
#         return
#     def checkout(self, dog):
#         self.dogs.remove(dog)
#         print(f"{dog.name}, checked out")
#         return
#     def greeting(self):
#         for dog in self.dogs:
#             dog.bark(1)
#
# dog1 = Dog("Bruno", 5)
# dog2 = Dog("Tyson", 2)
# dog3 = Dog("Astor", 9, "av av")
#
# hotel = Hotel()
# hotel.checkinn(dog1)
# hotel.checkinn(dog2)
# hotel.greeting()
#
# hotel.checkout(dog1)
# hotel.checkinn(dog3)
# hotel.greeting()

# #STUDENT CLASS WITH ATTENDANCE:
# class Student:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#     def greeting(self, name):
#         print(f"Hello {name}, welcome to the class")
#
# class Teacher:
#     def __init__(self):
#         self.attendance = []
#     def present(self, student):
#         self.attendance.append(student)
#         print(f"The student {student.name} is present for the class")
#         return
#     def absent(self, student):
#         self.attendance.remove(student)
#         print(f"The student {student.name} has left the class")
#         return
#     def welcome(self):
#         for student in self.attendance:
#             student.greeting(student.name)
#         return
#
# teacher = Teacher()
#
# name = str(input("Please enter the students name, or press enter to exit:  "))
# while name != "":
#     last_name = str(input("Please enter the students last name: "))
#     student = Student(name, last_name)
#     present = str(input("Enter 'p' for present or 'a' for absent: "))
#     if present == "p":
#         teacher.present(student)
#     elif (present == "a") and (student in teacher.attendance) == True:
#         teacher.absent(student)
#     else:
#         print("Error occured")
#     name = str(input("Please enter the next student name, or press enter to exit:  "))
#
# teacher.welcome()


#CAR WASH ASSOCIATION:
class Car:
    def __init__(self, model, registration, color):
        self.model = model
        self.registration = registration
        self.color = color
class PaintShop:
    def paint(self, car, color):
        car.color = color

paint_shop = PaintShop()
car = Car("Opel", "BG-128", "black")
print(f"The current color of the car is {car.color}")
paint_shop.paint(car, "green")
print(f"The new color of the car is {car.color}")













































































































