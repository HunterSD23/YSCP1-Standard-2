# tip_calculator.py
# A simple tip calculator to compute tip amount and total bill

def main():
    def get_bill_amount():
        bill_amount = float(input("Enter the bill amount: $"))
        if bill_amount > 0:
            return bill_amount
        else:
            print("Error: Invalid Input. Please Try Again.")
        
    def get_tip_amount():
        tip_percentage = int(input("Enter the tip percentage (e.g., 15 for 15%): "))
        if tip_percentage > 0:
            return tip_percentage
        else:
            print("Error: Invalid Input. Please Try Again.")

        tip_amount = (tip_percentage / 100) * bill_amount
        return tip_amount

    def calculate_total_bill():
        total_bill = bill_amount + tip_amount
        return total_bill
    
    print("\n---------- Welcome to the Tip Calculator! ----------\n")
    
    bill_amount = get_bill_amount()
    tip_amount = get_tip_amount()

    total_bill = calculate_total_bill()

    print("\n--- Tip Calculator Summary ---")
    print(f"Bill Amount: ${bill_amount:.2f}")
    print(f"Tip Amount:  ${tip_amount:.2f}")
    print(f"Total Bill:  ${total_bill:.2f}")

    print("Thank you for using the Tip calculator\n")

main()