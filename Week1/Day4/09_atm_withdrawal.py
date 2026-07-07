balance = 10000
withdrawal_amount = int(input("Enter the amount to withdraw: "))
if withdrawal_amount <= 0:
    print("Invalid withdrawal amount")
elif withdrawal_amount % 100 != 0:
    print("Invalid withdrawal amount. Please enter an amount in multiples of 100.")
elif withdrawal_amount > balance:
    print("Insufficient balance")
else:
    balance -= withdrawal_amount
    print(f"Withdrawal successful. Remaining balance: {balance}")        
