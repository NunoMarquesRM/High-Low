from art import logo, vs
from game_data import data
from random import randrange

def random_choice():
    indexA = randrange(len(data))
    indexB = randrange(len(data))
    while indexB == indexA:
        indexB = randrange(len(data))
    return data[indexA], data[indexB]

def compare(data_a, data_b, choice_user):
    if data_a >  data_b:
        return choice_user == "a"
    else:
        return choice_user == "b"

def game_prints(compare_a, compare_b):
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
    print(vs)
    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
    return compare(compare_a['follower_count'], compare_b['follower_count'], input("Who has more followers? Type 'A' or 'B': ").lower())

def game_score(running):
    global SCORE
    if running:
        SCORE += 1
    else:
        running = False
    return running

def validation(run):
    if run:
        print(f"You're right! Current score {SCORE}")
    else:
        print(f"Sorry, that's wrong. Final score: {SCORE}.")

def main():
    print(logo)
    optionA, optionB = random_choice()
    game_is_running = game_score(game_prints(optionA, optionB))
    validation(game_is_running)
    
    while game_is_running:
        # Clear the screen
        print("\n" * 20)
        print(logo)
        validation(game_is_running)
        optionA, optionB = random_choice()
        game_is_running = game_score(game_prints(optionA, optionB))
        validation(game_is_running)

SCORE = 0
main()