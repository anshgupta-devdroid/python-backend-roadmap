english_marks = int(input("Enter English marks: "))
maths_marks = int(input("Enter Maths marks: "))
science_marks = int(input("Enter Science marks: "))
social_marks = int(input("Enter Social marks: "))
hindi_marks = int(input("Enter Hindi marks: "))
total_marks = english_marks + maths_marks + science_marks + social_marks + hindi_marks
average_marks = total_marks / 5
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")               
# if average_marks >= 90:
#     print("A")
# elif average_marks == 89 or average_marks >= 75:
#     print("B")
# elif average_marks == 74 or average_marks >= 60:
#     print("C")
# elif average_marks < 60:
#     print("D")
# else:
#     print("Fail") 