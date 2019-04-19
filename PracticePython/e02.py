def get_number():
    try:
        number = int(input('Enter a number: >'))
    except:
        print("Please enter an integer")
        return  get_number()
    return number

def calculate(number):
    try:
        if number % 4 == 0:
            return 'super even'
        elif number % 2 == 0:
            return 'even'
        else:
            return 'odd'
    except:
        print('something went wrong..')
        exit(1)

def main():
    number = get_number()
    odd_or_even = calculate(number)
    print(f'Your number is {odd_or_even}')

main()
