import json

LANGUAGE = 'en'
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message):
    return MESSAGES[LANGUAGE][message]

def prompt(messages):
    print(f'==> {messages}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True  
    return False

def another_calculation():
    prompt(messages("another_calculation_prompt"))
    answer = input().lower()
    while answer not in ['y', 'n']:
        prompt(messages("invalid_another_calculation"))
        answer = input().lower()
    if answer == 'y':
        return True
    elif answer == 'n':
        return False

prompt(messages("welcome"))

while True:

    prompt(messages("first_number_prompt"))
    number1 = input()

    while invalid_number(number1):
        prompt(messages("invalid_number"))
        number1 = input()


    prompt(messages("second_number_prompt"))
    number2 = input()

    while invalid_number(number2):
        prompt(messages("invalid_number"))
        number2 = input()

    prompt(messages("operation_prompt"))
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(messages("invalid_operation"))
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1)/float(number2)

    print("==>",messages("result") + str(output))

    if another_calculation():
        continue
    else:
        prompt(messages("thank you"))
        break