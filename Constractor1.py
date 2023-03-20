# creating instance which save the id when create the object
class student: # class is a templet which contain class name , attribute and method
    def SayHello():
        print("Hello")
Abebe=student()
Desatw=student()
print(id(Abebe)) # memory address of Abebe
print(id(Desatw)) # memmory address or Id of Desatw 
# creat for all student insatance by using self method
class student:
    def SayHello(self): 
        print("Hello")
Abebe=student()
Desatw=student()
Abebe.SayHello()
Desatw.SayHello()

# Creat any unkonw student as an instance
class student:
    def SayHello(self): 
        print("Hello")
s1=student()
s2=student()
s1.SayHello()
s2.SayHello()
# self means current object and used to pass on the method
class student:
    def SayHello(self): 
        print("Hello" + " " + self.FName)
s1=student()
s2=student()
s1.FName="Desatw"
s1.SayHello()
# constractor creating an object 
class student:
    def __init__(self,Fn,Ln):
        self.Fname=Fn
        self.Lname=Ln
    def SayHello(self):
        print("Hello" + " " +self.Fname + " " +self.Lname )
        
s1=student("Abeeb","Taddes")
s1.SayHello()
s2=student("Desatw","Gisme")
s2.SayHello()
# add addtional class 
class student:
    def __init__(self,Fn,Ln):
        self.Fname=Fn  # attribute 
        self.Lname=Ln  # attribute
        school="Destaw International Software Solution"
    def SayHello(self): # method 
        print("Hello" + " " +self.Fname + " " +self.Lname )
    def GetFullNameEth(self): # behavor or methods
        print (self.Fname +" " + self.Lname)
    def GetFullNameEur(self): # method
        print ("in eroupe" +" " +self.Lname+" " + self.Fname)
        
# s1=student("Abeeb","Taddes")
# s1.GetFullNameEth()
# s1.GetFullNameEur()
s2=student("Desatw","Gisme")
s2.GetFullNameEur()
s2.GetFullNameEth()
