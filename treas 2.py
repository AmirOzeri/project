

import random
import csv
import os
def create_textbox():
    numbers = list(range(10))
    textbox = ''
    for num in numbers:
        count = random.randint(1, 20)
        textbox += str(num) * count
    textbox += 'TREASURE'
    for num in reversed(numbers):
        count = random.randint(1, 20)
        textbox += str(num) * count

    return textbox
def create_file(new_file,textbox):
    file = open(new_file, 'w')
    file.write(textbox)

def create_top10_results(results_file):
    if not os.path.exists(results_file):
        # If the 'top10_results.csv' file doesn't exist, create it with an empty header row
        with open(results_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Player Name', 'Tries'])
    with open(results_file, 'r') as file:
        # DictReader allows me to read dictionaries into the csv file
        reader = csv.DictReader(file)
        top10_results = list(reader)    # making reader a list of dictionary
    top10_results.sort(key=get_tries)  # Sort based on number of tries
    top10_results = top10_results[:10]  # Keep only the top 10 results
    return top10_results

def get_tries(result):
    return int(result['Tries'])

def add_result(top10_results, player_name, tries):
    top10_results.append({'Player Name': player_name, 'Tries': tries})
    top10_results.sort(key=get_tries)  # Sort based on number of tries
    top10_results[:] = top10_results[:10]  # Keep only the top 10 results in place
    return top10_results

def update_top10_results(file_name, top10_results):
        file = open(file_name, 'w', newline='')
        # setting the headers for the results table
        results_table = ['Player Name', 'Tries']
        # DictWriter allows me to write dictionaries into the csv file
        writer = csv.DictWriter(file, fieldnames=results_table)
        # using writeheader in order to have the headers on top
        writer.writeheader()
        # using writerows in order to have each result in different row
        writer.writerows(top10_results)

def find_the_treasure(new_file):
    file = open(new_file, 'r')
    textbox = file.read()
    treasure_letters = list('TREASURE')
    cursor = 0
    tries = 0
    while all(textbox[cursor] != treasure_letters[i] for i in range(len(treasure_letters))):
        direction = int(input('Where do you want to move? (1 - forward, 2 - backward) '))
        steps = int(input('How many characters? '))
        if direction == 1:
            if (cursor + steps) >= len(textbox):
                cursor = len(textbox) - 1
            else:
                cursor += steps
        elif direction == 2:
            if (cursor - steps) < 0:
                cursor = 0
            else:
                cursor -= steps
        if textbox[cursor] not in treasure_letters:
            print(f'you hit {textbox[cursor]} try again until you hit one of the TREASURE letters')
        tries += 1
    print(f'Congratulations!! you found the TREASURE it took you {tries} tries to find it')
    player_name = input('Enter your name: ')
    add_result(top10_results, player_name, tries)
    update_top10_results(results_file, top10_results)


# Calling for the functions
results_file = 'top10_results.csv'
top10_results = create_top10_results(results_file)
file_name = 'treasure_hunt.txt'
text = create_textbox()
create_file(file_name, text)
find_the_treasure(file_name)