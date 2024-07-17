def main():
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? : $"))
    tip = int(input("What percentage tip would you like to give? 10, 12, or 15? : "))
    people = int(input("How many people to split the bill? : "))
    
    total_bill = bill + bill * (tip / 100)
    bill_each = total_bill / people
    final_amount = "{:.2f}".format(bill_each)
    
    print(f"\nEach person should pay : ${final_amount}")
    
    
main()