import math
import random

def generate_randomized(min, max, how_many):
    random_numbers = []
    for i in  range(how_many):
        random_numbers.append(random.randint(min, max))
    return random_numbers

def ask_for_numbers(range_from,range_to):
    return int(input(f'Enter an number from{range_from} to {range_to}: '))

def guess_game(min, max, how_many = 10):
    random_numbers = generate_randomized(min, max, how_many)
    for i in range(len(random_numbers)):
        user_guess_number = ask_for_numbers(min, max)
        while random_numbers[i] != user_guess_number:
            if user_guess_number < random_numbers[i]:
                print('guess is low')
                user_guess_number = ask_for_numbers(min, max)
            elif user_guess_number > random_numbers[i]:
                print('guess is high')
                user_guess_number = ask_for_numbers(min, max)
            else:
                break
        print("you guessed it!")
guess_game(1, 99)
#guess_game(1, 49)

