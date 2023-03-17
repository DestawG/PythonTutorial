# list is a collection which is ordered and changeable . allows duplicate members
list=["Abebe","Destaw","Mulugeta","Destaw"]
list[0]="Tedy"
print(list)
print(list[0])
print(list[-1])
print(list[0:3])
# tuble is a  collection which is ordered and unchangeable. allows duplicate members
tuble=("Abebe","Destaw","Mulugeta","Destaw")
print(tuble)
print(tuble[0])
# set is a  collection which is unordered and unindexed. no duplicate members
set={"Abebe","Destaw","Mulugeta","Destaw"}
print(set)
# dictionary is a collection which is unordered, changeable and indexed. no duplicate members
student= {  "firstName":"Destaw",
             "lastName":"Mulachew",
             "email": "destawg@gmail.com"
}
print(student["firstName"]+ student["lastName"])
# to remove 
student.pop("email")
# to add something 
student["Gendar"]="Male"
print(student)



             

