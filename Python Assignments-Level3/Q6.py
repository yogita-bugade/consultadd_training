'''Create the custom Python classes which have methods and
attributes and implement single inheritance, multiple inheritance,
and multilevel inheritance'''
#Single Inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()

#Multiple Inheritance

class A:
    def method_A(self):
        print("Method from class A")

class B:
    def method_B(self):
        print("Method from class B")

class C(A, B):
    def method_C(self):
        print("Method from class C")

c = C()
c.method_A()
c.method_B()
c.method_C()

# Multilevel Inheritance
class A:
    def method_A(self):
        print("Method from class A")

class B(A):
    def method_B(self):
        print("Method from class B")

class C(B):
    def method_C(self):
        print("Method from class C")

c = C()
c.method_A()
c.method_B()
c.method_C()
