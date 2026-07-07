student_marks = int(input("Enter the student's marks: "))
if student_marks < 0 or student_marks >100:
     print("Result : Invalid marks")
elif student_marks >= 40:
    print("Result : Pass")
else:
    print("Result : Fail")