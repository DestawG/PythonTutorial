# Object orunted programming 
# calss is the blue print or layout 
# object representation of real world or an instance of the class
# object orinted is object based 
# progreaming is the set of instractution 
# example student (class),list of student is an object 
# procedural programming(pp) also known as inline programming takes a top-down approach
# Functional programming(FP) is also a bout passing sdata from function  to function to get a result
# onbejct orinted programming is a programming paradigm based on the concept of "object", which may contain data, in the form of fields, often known as attributes, and code in the form of prcedures, often known as methods.
# python is both procidural and functional language 
# object orinted programming has two basic componenets
    # attribute - stored in avaribele or properties
     # Behavior-Methods
# constractor creating new instance or creating an object 
# class Student: # class
#     def greetings(self): # self means current object 
#         print("Hello"+ self.Fname)
# s1=Student() 
# s2=Student()  
# s1.Fname="Desatw" 
# s1.greetings() 
# Abebe =Student()
# Destaw=Student()
# Destaw.greetings()
# print (id (Abebe)) # creating instance
# print(id(Destaw))

# to create constracture we will use _init 
class student: 
   def _init_(self, fn, ln): 
       self.Fname= fn
       self.Lname= ln
def SayHello(self):
        print("Hello" +self.Fname + "" + self.Lname)
        
s1=student("Destaw","Gisme") 
s1.SayHello()
s2=student("Abebe","Tadees") 
s2.SayHello()

# s1.GetFullName()
# s2.GetFullName()
        
