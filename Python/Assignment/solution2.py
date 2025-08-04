student_grade = { 
                  'manish':90,
                  'varun':80,
                  'bhanu':33,
                  'surya':50
                  }
# add a new student and grade
student_grade["versha"] = 80
print(student_grade)

# update an existing student's grade
student_grade['surya'] = 40
student_grade.update({'bhanu':30})
print(student_grade)

# print all student grades.
for i in student_grade:
    print(student_grade[i])


#print all students name and grades
for key,value in student_grade.items():
    if value >=33:
        print(f"{key} with {value} marks is pass")
    else:
        print(f"{key} with {value} marks is fail")
    
