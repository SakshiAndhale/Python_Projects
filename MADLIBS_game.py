#String concatenation aka how to put strings together

def get_word(prompt):
    return input(prompt)

def main():
    # Prompts to get words from the user
    adjective1 = get_word("Enter an adjective: ")
    adjective2 = get_word("Enter another adjective: ")
    noun1 = get_word("Enter a noun: ")
    noun2 = get_word("Enter another noun: ")
    plural_noun = get_word("Enter a plural noun: ")
    game = get_word("Enter a game: ")
    plural_noun2 = get_word("Enter another plural noun: ")
    verb_ending_in_ing = get_word("Enter a verb ending in 'ing': ")
    verb_ending_in_ing2 = get_word("Enter another verb ending in 'ing': ")
    plural_noun3 = get_word("Enter one more plural noun: ")
    verb_ending_in_ing3 = get_word("Enter another verb ending in 'ing': ")
    noun3 = get_word("Enter another noun: ")
    plant = get_word("Enter a type of plant: ")
    body_part = get_word("Enter a part of the body: ")
    place = get_word("Enter a place: ")
    verb_ending_in_ing4 = get_word("Enter another verb ending in 'ing': ")
    adjective3 = get_word("Enter another adjective: ")
    number = get_word("Enter a number: ")
    plural_noun4 = get_word("Enter one last plural noun: ")

    # Story template
    story = f"""
    A vacation is when you take a trip to some {adjective1} place with your {adjective2} family. 
    Usually you go to some place that is near a/an {noun1} or up on a/an {noun2}. 
    A good vacation place is one where you can ride {plural_noun}. 
    I like to spend my time {verb_ending_in_ing} or {verb_ending_in_ing2}. 
    When parents go on a vacation, they spend their time eating three {plural_noun2} a day, 
    and fathers play golf, and mothers sit around {verb_ending_in_ing3}. 
    Last summer, my little brother fell in a/an {noun3} and got poison {plant} all over his {body_part}. 
    My family is going to go to (the) {place}, and I will practice {verb_ending_in_ing4}. 
    Parents need vacations more than kids because parents are always very {adjective3} 
    and because they have to work {number} hours every day all year making enough {plural_noun4} to pay for the vacation.
    """

    print(story)

if __name__ == "__main__":
    main()
