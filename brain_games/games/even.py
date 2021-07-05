from random import randint


def even_game():
    ask_num = randint(1, 100)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print("Question: {}".format(ask_num))
    prompt.string('Your answer: ')


even_game()