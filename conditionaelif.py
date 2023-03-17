# student grade 
# sR> 90 "a",SR>80 "B",SR>70,"C",SR>60,"D",SR<=60,"F"
mark=int(input("please enter grade?"))
if mark>= 90:
    grade="A"
elif mark >= 80:
    grade="B"
elif mark>=70:
    grade="C"
elif mark>60:
    grade="D"
else :
    grade="F"
print(grade)
 