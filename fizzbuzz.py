print('FizzBuzz')

user_input = input('Enter a number: ')

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz!')
    elif num % 3 == 0:
        print('Fizz!')
    elif num % 5 == 0:
        print('Buzz!')
    else:
        print(' :( ')

fizz_buzz(int(user_input))
