import prompt
from brain_games.scripts.brain_games import greeting


def engine(module):
    greeting()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(module.GAME_QUESTION)
    counter = 0
    while counter < 3:
        (question, correct_answer) = module.generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
