
def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def get_loan_duration():
    prompt("Please enter your loan duration in months")
    loan_duration = input()
    while invalid_number(loan_duration) or float(loan_duration) <= 0:
        prompt("Invalid input. Please enter a valid loan duration in months")
        loan_duration = input()
    loan_duration = int(loan_duration)
    return loan_duration


def get_loan_amount():
    prompt("Please enter your car loan amount! e.g 15000")
    loan_amount = input()
    while invalid_number(loan_amount) or float(loan_amount) <=0:
        prompt("Invalid input. Please enter a valid number.")
        loan_amount = input()
    loan_amount = round(float(loan_amount), 2)
    return loan_amount

def get_interest_rate():
    prompt("Please enter your annual interest rate")
    interest_rate = input()
    while invalid_number(interest_rate) or float(interest_rate) < 0:
        prompt("Invalid input. Please enter your annual interest rate.")
        interest_rate = input()
    interest_rate = float(interest_rate)
    return interest_rate

def monthly_payment_calculator(loan, interest, duration):
    if interest_rate != 0:
        monthly_interest_rate = ((interest) / 12) / 100
        principle = (monthly_interest_rate)
        times_compounded = (1-((1+monthly_interest_rate)**(-duration)))
        monthly_payment = loan * (principle/times_compounded)
    else:
        monthly_payment = loan / duration

    prompt(f'Loan = ${loan}')
    prompt(f'Annual interest rate = {interest}% (compounded monthly)')
    prompt(f'Loan duration = {duration} months')
    prompt(f'Your monthly payment is ${round(monthly_payment, 2)}')

def another_calculation():
    prompt("Do you need help with another loan? (y/n)")
    answer = input().lower()
    while answer not in ['y', 'n']:
        prompt("That is not a valid response. Please enter 'y' or 'n' ")
        answer = input().lower()
    return answer =='n'

while True:
    prompt("Welcome to the Car Loan Caclulator!")
    loan_amount = get_loan_amount()

    interest_rate = get_interest_rate()

    loan_duration = get_loan_duration()

    monthly_payment_calculator(loan_amount, interest_rate, loan_duration)

    if another_calculation():
        prompt("Thank you! I hope we were helpful!")
        break