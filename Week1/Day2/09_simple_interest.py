principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the rate of interest : "))
time = float(input("Enter the time in years : "))

interest = (principal * rate * time) / 100
final_amount = principal + interest

print("===== SIMPLE INTEREST =====")
print(f"Principal   : {principal}")
print(f"Rate        : {rate}")
print(f"Time        : {time}")
print("---------------------------")
print(f"Interest    : {interest:.2f}")
print(f"Final Amount: {final_amount:.2f}")
print("==========================")