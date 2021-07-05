import random
from brain_games.cli


def main():
    i = 1
    while i <= 3:
        num = random.randint(1, 100)
        correct_answer = 'no'
        if num % 2 == 0:
            correct_answer = 'yes'
        print("Question: {}".format(num))
        reply = input('Your answer: ')

        if reply == correct_answer:
            print("Correct!")

        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                reply, correct_answer))
            print("Let's try again, {}!".format(brain_games.cli.get_name))
            return
        i = i + 1
    print('Congratulations, {}!'.format(brain_games.cli.get_name))


if __name__ == "__main__":
    main()