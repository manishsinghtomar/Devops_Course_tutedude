age = int(input("enter \n your age: \n"))

print(type(age))

if age == 18:
    print("yes, you are 18")

else: 
    print("yes, you are not 18")

marks = float(input("enter your marks \n"))

if marks >= 90:
    grade = "A"
elif marks >=80:
    grade = "B"
elif marks >=70:
    grade = "C"
elif marks >=60:
    grade = "D"
elif marks >=50:
    grade = "E"
print("your grade:",grade)
# print("your grade: "+grade)