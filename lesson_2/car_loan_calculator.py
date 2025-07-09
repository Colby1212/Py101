
def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False
    

def monthly_payment_calculator(annual_interest_rate, loan_amount, loan_duration):
    annual_interest_rate = float(annual_interest_rate)
    loan_amount = float(loan_amount)
    loan_duration = int(loan_duration)
    interest_rate = float(annual_interest_rate) / 12
    monthly_payment = float(loan_amount) * (((interest_rate)) / (1- (1 +(interest_rate)) ** (-float(loan_duration))))
    print(round((monthly_payment), 2))


prompt("Welcome to the Car Loan Caclulator!")

prompt("Please enter your car loan amount! e.g 15000")
loan_amount = input()
while invalid_number(loan_amount) or (float(loan_amount) <= 0):
    prompt("Invalid input. Please enter a valid car loan amount")
    loan_amount = input()

prompt("Please enter your annual interest rate (5.5% = 5.5 not 0.055)")
annual_interest_rate = input()
while invalid_number(annual_interest_rate) or float(annual_interest_rate) <= 0:
    prompt("Invalid input. Please enter a valid annual interest rate (5.5% = 5.5 not 0.055).")
    annual_interest_rate = input()

prompt("Please enter your loan duration in months")
loan_duration = input()
while invalid_number(loan_duration) or float(loan_duration) <= 0:
    prompt("Invalid input. Please enter a valid loan duration in months")
    loan_duration = input()
monthly_payment_calculator()



