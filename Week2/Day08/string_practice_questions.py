# Count spaces in a sentence
user = input("Enter any sentence : ")
count = 0
for ch in user:
    if ch == " ":
        count += 1
print(count)
 
# Count digits in a string
user = input("Enter anything : ")
count = 0
for ch in user:
  if ch.isdigit():
    count += 1
print(count)

# Convert first and last character to uppercase
name = "python"
print(name[0].upper() + name[1:-1]  + name[-1].upper())

# Count number of words
name = input("Enter your sentence : ")
new_name = name.split()
for i in new_name:
    print(i)
print(len(new_name))
