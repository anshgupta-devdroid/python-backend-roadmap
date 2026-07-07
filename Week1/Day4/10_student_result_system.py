student_name = input("Enter the student's name: ")
student_marks = int(input("Enter the student's marks: "))
if student_marks < 0 or student_marks > 100:
    print(f"Result for {student_name}: Invalid marks")
elif student_marks >= 90 and student_marks <= 100:
    if student_marks == 100:
       print("Perfect score! Congratulations!")
    print(f"Result for {student_name}: Grade : A, Result : Pass , Excellent performance")
elif student_marks >= 75 and student_marks <= 89:
    print(f"Result for {student_name}: Grade : B, Result : Pass")
elif student_marks >= 60 and student_marks <= 74:
    print(f"Result for {student_name}: Grade : C, Result : Pass")
elif student_marks >= 40 and student_marks <= 59:
    print(f"Result for {student_name}: Grade : D, Result : Pass")
else:
    print(f"Result for {student_name}: Grade : F, Result : Fail , Need improvement")    