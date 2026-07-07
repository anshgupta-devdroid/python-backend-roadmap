user_total_marks = int(input("Enter the total marks: "))
if user_total_marks < 0 or user_total_marks > 100:
    print("Invalid marks")
elif user_total_marks >= 90 and user_total_marks <= 100:
    print("Grade : A")
    print("Result : Pass")
elif user_total_marks >= 75 and user_total_marks <= 89:
    print("Grade : B")
    print("Result : Pass")
elif user_total_marks >= 60 and user_total_marks <= 74:
    print("Grade : C")
    print("Result : Pass")
elif user_total_marks >= 40 and user_total_marks <= 59:
    print("Grade : D")
    print("Result : Pass")
else:
    print("Grade : F")
    print("Result : Fail")        
