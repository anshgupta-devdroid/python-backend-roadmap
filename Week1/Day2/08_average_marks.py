math_marks = float(input("Enter marks in Math : "))
science_marks = float(input("Enter marks in Science : "))
english_marks = float(input("Enter marks in English : "))

total_marks = math_marks + science_marks + english_marks
average_marks = total_marks / 3

print("===== STUDENT RESULT =====")
print(f"Math     : {math_marks}")
print(f"Science  : {science_marks}")
print(f"English  : {english_marks}")
print("-------------------------")
print(f"Total    : {total_marks}")
print(f"Average  : {average_marks:.2f}")
print("==========================")