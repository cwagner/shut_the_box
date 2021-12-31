#!/usr/bin/env python3
import os
import random

from dice import print_dice


def main():
    print("Let's play shut the box!")
    print("How many players do you have?")
    players = int(input())
    scores = []
    for p in range(players):
        box = [True for _ in range(9)]
        while any(box):
            _clear_screen()
            print(f'Player {p + 1}:')
            _print_values(box)
            print()
            print("Dice roll:")
            roll_1 = random.randint(1, 6)
            roll_2 = random.randint(1, 6)
            print_dice(roll_1, roll_2)
            die_sum = roll_1 + roll_2
            print(f'Sum: {die_sum}')
            print("Type the numbers you'd like to put down, separated by a comma")
            # TODO: predict if valid input is possible
            nums = _parse_input(input())

            if sum(nums) == die_sum and _valid_selections(nums, box):
                for num in nums:
                    box[num - 1] = False
            else:
                score = _score(box)
                print(f"You're done! Your score is {score}")
                scores.append(score)
                break

        if not any(box):
            print('You shut the box!!')
            # TODO: end game here?
            scores.append(0)
        print('Press enter to proceed')
        input()

    # TODO: handle ties
    print('Final scores:')
    for i, score in enumerate(scores):
        print(f'Player {i + 1}: {score}')
    print(f'Player {scores.index(min(scores)) + 1} wins!!')


def _clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def _print_values(box):
    values = [str(_get_value(box, i)) for i in range(len(box))]
    print("|" + "|".join(values) + "|")


def _get_value(box, index):
    return index + 1 if box[index] else "x"


def _parse_input(raw_string):
    return [int(num.strip()) for num in raw_string.split(',')]


def _valid_selections(nums, box):
    # All entered numbers are within range
    # And all are "on" in the box
    return all(num <= len(box) for num in nums) and \
           all(flag is True for flag in [box[val - 1] for val in nums])


def _score(box):
    return sum([i + 1 for i in range(len(box)) if box[i]])


if __name__ == '__main__':
    main()
