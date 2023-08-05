
import time
import random

quotes_list = [
    ['always', 'be', 'yourself'],
    ['keep', 'it', 'cool'],
    ['dream', 'big', 'achieve'],
    ['love', 'laugh', 'live'],
    ['never', 'give', 'up'],
    ['learn', 'grow', 'evolve'],
    ['stay', 'true', 'you'],
    ['live', 'love', 'laugh'],
    ['life', 'is', 'beautiful'],
    ['think', 'positive', 'thoughts']
]


def random_quote(quote_list):       # בחירת משפט רנדומלית
    random_index = random.randrange(0,len(quote_list))
    return quote_list[random_index]

def create_new_list(quote):         #  יצירת רשימה של קו תחתון באורך המשפט
    guess = []
    for word in quote:
        guess.append('_' * len(word))
    return guess



def update_new_list(new_list, quote, letter,):       # הצגת הרשימה עם האותיות שנבחרו
    for i in range(len(quote)):
        for j in range(len(quote[i])):
            if quote[i][j]== letter:
                new_list[i] = new_list[i][:j] + letter + new_list[i][j+1:]
    return new_list



def game():
    quote = random_quote(quotes_list)
    new_list = create_new_list(quote)
    tries = []
    correct_guesses = 0
    wrong_guesses = 0
    print('wellcome to the Guess-The-Word game!')
    print('try to guess the three-word quote:')
    start_time = time.time()
    while quote != new_list:
        print(new_list)
        guess = input('enter a letter:').lower()
        updated_list = update_new_list(new_list, quote, guess)
        if guess in ' '.join(updated_list) and guess not in ' '.join(tries):
            tries.append(guess)
            correct_guesses += 5
        else:
            wrong_guesses -= 1
    score = correct_guesses + wrong_guesses +100
    end_time = time.time()
    if end_time - start_time > 30:
        score -=100
    print(f'congratulations! you guessed the quote!, your quote is {quote}')
    print(f'total points:{score}')

game()





