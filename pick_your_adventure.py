"""
Author: Kae Clayton
Purpose: Create and adventure game using multiple
functions and modules to show my range of skills
"""

import random
import csv
import os
import string

NOUNS = {
        "space": {
            "single": ["alien", "comet", "space junk", "space dog", 
                    "astronaut", "Rocket", "Groot", "C3PO", "R2D2"],
            "plural": ["aliens", "comets", "rockets", "space dogs", "astronauts",
                    "Guardians of the Galaxy", "droids", "Storm Troopers"]
        },
        "ocean": {
            "single": ["great white shark", "giant squid", "sperm whale", 
                    "pufferfish", "scuba diver", "submarine", "orca"],
            "plural": ["great white sharks", "giant squids", "sperm whales",
                    "pufferfish", "scuba divers", "submarines", "orcas"]
        },
        "jungle": {
            "single": ["macaw", "jaguar", "mosquito", "monkey",
                    "feral child", "jungle vine", "man eating plant"],
            "plural": ["macaws", "jaguars", "mosquitoes", "monkeys",
                    "feral children", "jungle vines", "man eating plants"]
        }
    }

def main():
    print("\nWelcome to Pick Your Adventure\n")
    
    letter_index = 0
    female_index = 1
    male_index = 2


    print ("Let's get your character's name\n")
    name_dict = get_name_dictionary("character_name.csv", letter_index)

    if not name_dict:
        print("Can't start the game without the character names file.")
        return

    gender_choice = ask_choice("Do you want a male or female character? (m/f) ", ["m", "f"])
    character_choice = ask_choice("To get your character's name pick a letter from A-Z: ", list(string.ascii_lowercase))
    
    if gender_choice == "m":
        char_name = get_character_name(name_dict, male_index, character_choice)
    elif gender_choice == "f":
        char_name = get_character_name(name_dict, female_index, character_choice)

    print (f"Your name is {char_name}.\n")      
    
    adventures_list = ["Space Adventure", "Ocean Adventure", "Jungle Adventure", "Random Adventure"]
    print ("Now let's choose which type of adventure you will be having.\n")
    print ("Available adventures are:")
    for adventure in adventures_list:
        print (adventure)
        
    adventure_choice = ask_choice("Which adventure do you choose? (space/ocean/jungle/random) ", ["space", "ocean", "jungle", "random"])
    
    tense = random.choice(["past", "present", "future"])
    quantity = random.choice([1, 2, 3, 4, 5])

    if adventure_choice == "random":
        adventure_choice = random.choice(["space", "ocean", "jungle", "mixed"])

    story_titles = {
        "space": "Random Space Story",
        "ocean": "Random Ocean Story",
        "jungle": "Random Jungle Story",
        "mixed": "Completely Random Story"
    }

    if adventure_choice == "mixed":
        themes = ["space", "ocean", "jungle"]
    else:
        themes = [adventure_choice]

    print(f"Hello {char_name}! Welcome to the {story_titles[adventure_choice]}. Enjoy!\n")
    tell_story(themes, quantity, tense)                                            

def ask_choice(prompt, valid_answers):
    """Ask the player a question until they give a valid answer.
    Parameters
        prompt: the question to show the player
        valid_answers: a list of acceptable answers
    Return: the player's answer in lowercase
    """
    while True:
        answer = input(prompt).strip().lower()

        if answer in valid_answers:
            return answer

        print(f"Please choose one of: {', '.join(valid_answers)}")

def get_name_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary"""
    dictionary = {}
    
    try:
        with open(filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip header row
            
            for row in reader:
                if len(row) >= 3:  # Ensure we have enough columns
                    key = row[key_column_index].strip().upper()
                    dictionary[key] = row
            
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found in: {os.getcwd()}")
        return {}
    
    return dictionary


def get_character_name(dictionary, index, letter):
    """Find a character name in the name dictionary
    Parameters:
        dictionary: the dictionary that stores character names as a value and the
            alphabet letter as the key
        index: the position of the name in that letter's row, 
            1 for the female name or 2 for the male name
        letter: the letter the player chose, in either case; 
            it is changed to uppercase to match the dictionary keys
    Return: The character name
    """

    letter = letter.upper()
    character_name = "Alex Adventurer"

    if letter in dictionary:
        character_name_list = dictionary[letter]
        character_name = character_name_list[index]

    return character_name    

def make_sentence(theme, quantity, tense, with_phrase=True):
    """Build and return a sentence, either short or long:
    the short sentence will have a determiner, an adjective, a noun, an adverb, and a
    verb. The long sentence will add a prepositional phrase.  The grammatical quantity 
    of the determiner and noun will match the number in the quantity parameter. The 
    grammatical quantity and tense of the verb will match the number and tense in the 
    quantity and tense parameters.
    Parameters:
        theme: the type of adventure for the sentence
        quantity: an integer (to determine single or plural nouns)
        tense: past, present, or future verb tense
        with_phrase: a Boolean to determine if there is a prepositional phrase added
    """

    determiner = get_determiner(quantity).capitalize()
    noun = get_noun(theme, quantity)
    verb = get_verb(quantity, tense)
    adjective = get_adjective()
    adverb = get_adverb()

    sentence = f"{determiner} {adjective} {noun} {adverb} {verb}"

    if with_phrase:
        prepositional_phrase= get_prepositional_phrase(theme, quantity)
        sentence += f" {prepositional_phrase}"

    return sentence + "."

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the", "that", "this"]
    else:
        words = ["some", "many", "the", "these", "those"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(theme, quantity):
    """Return a randomly chosen noun for the given theme.
    Parameters
        theme: "space", "ocean", "jungle"
        quantity: 1 for a single noun, anything else for plural
    Return: a randomly chosen noun
    """
    if quantity == 1:
        return random.choice(NOUNS[theme]["single"])
    else:
        return random.choice(NOUNS[theme]["plural"])
    
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "growled", "ran", "chuckled", "balked", "coughed",
        "sang", "broke", "fought", "believed", "needed"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "growls", "runs", "chuckles", "balks", "coughs",
        "sings", "breaks", "fights", "believes", "needs"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "growl", "run", "chuckle", "balk", "cough",
        "sing", "break", "fight", "believe", "need"
    If tense is "future", this function will return one of
    these ten verbs:
        "will growl", "will run", "will chuckle", "will balk",
        "will cough", "will sing", "will break", "will fight", 
        "will believe", "will need"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    
    past_tense_verbs = ["growled", "ran", "chuckled", "balked", "coughed",
        "sang", "broke", "fought", "believed", "needed"]
    present_single_verbs = ["growls", "runs", "chuckles", "balks", "coughs",
        "sings", "breaks", "fights", "believes", "needs"]
    present_plural_verbs = ["growl", "run", "chuckle", "balk", "cough",
        "sing", "break", "fight", "believe", "need"]
    future_tense_verbs = ["will growl", "will run", "will chuckle", "will balk",
        "will cough", "will sing", "will break", "will fight", 
        "will believe", "will need"]
    
    if tense == "past":
        verb = random.choice(past_tense_verbs)
    elif tense == "present" and quantity == 1:
        verb = random.choice(present_single_verbs)
    elif tense == "present" and quantity != 1:
        verb = random.choice(present_plural_verbs)
    elif tense == "future":
        verb = random.choice(future_tense_verbs)        
    
    return verb
    
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "for","from", "in", "into", 
        "near", "of","off", "on", "onto", "out", 
        "over", "to", "under", "with"
    Return: a randomly chosen preposition.
    """

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "for","from", "in", "into", 
        "near", "of","off", "on", "onto", "out", 
        "over", "to", "under", "with"]
    
    preposition = random.choice(prepositions)

    return preposition

def get_prepositional_phrase(theme, quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
        theme: the type of adventure
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.
    Return: a prepositional phrase.
    """

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(theme, quantity)

    prepositional_phrase = f"{preposition} {determiner} {noun}"

    return prepositional_phrase

def get_adjective():
    """Return a randomly chosen adjective from this
    list of adjectives:
        "adventurous", "ambitious", "angry", "calm",
        "confident", "easygoing", "helpful", "kind", "likeable",
        "polite", "quiet", "strong", "tenacious", "lazy",
        "scary", "fierce", "grumpy", "immense", "miniature"
    Return: a randomly chosen adjective
    """

    adjectives = ["adventurous", "ambitious", "angry", "calm",
        "confident", "easygoing", "helpful", "kind", "likeable",
        "polite", "quiet", "strong", "tenacious", "lazy",
        "scary", "fierce", "grumpy", "immense", "miniature"]
    
    adjective = random.choice(adjectives)

    return adjective

def get_adverb():
    """Return a randomly chosen adverb from this list
    of adverbs:
        "actively", "aggressively", "assertively", "boldly",
        "consistently", "curiously", "eagerly", "humorously",
        "quietly", "seriously", "successfully", "tactfully"
    Return: a randomly chosen adverb
    """

    adverbs = ["actively", "aggressively", "assertively", "boldly",
        "consistently", "curiously", "eagerly", "humorously",
        "quietly", "seriously", "successfully", "tactfully"]
    
    adverb = random.choice(adverbs)
    
    return adverb

def tell_story(themes, quantity, tense):
    """Build a story from randomly created sentences and prints it
    Parameters:
        themes: a list of themes; each sentence uses a random theme from it, so one theme
            makes a themed story and several make a mixed one.
        quantity: an integer
            a 1 indicates a singular noun, any other integer creates a plural noun
        tense:  the type of tense of the verbs in the sentence, past, present or future
    Return: nothing
    """

    first_paragraph = []
    second_paragraph = []

    for with_phrase in [True, False, False, True]:
        theme = random.choice(themes)
        first_paragraph.append(make_sentence(theme, quantity, tense, with_phrase=with_phrase))

    for with_phrase in [False, True, True, False]:
        theme = random.choice(themes)
        second_paragraph.append(make_sentence(theme, quantity, tense, with_phrase=with_phrase))

    print(" ".join(first_paragraph))
    print()
    print(" ".join(second_paragraph))
    print()

if __name__ == "__main__":
    main()  
