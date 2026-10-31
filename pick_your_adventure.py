"""
Author: Kae Clayton
Purpose: Create and adventure game using multiple
functions and modules to show my range of skills
"""

import random
import csv
import os

def main():
    print("\nWelcome to Pick Your Adventure\n")
    
    letter_index = 0
    female_index = 1
    male_index = 2

    print ("Let's get your character's name\n")
    gender_choice = input("Do you want a male or female character? (m/f) ").lower()
    character_choice = input("To get your character's name pick a letter from A-Z: ").lower()

    name_dict = get_name_dictionary("character_name.csv", letter_index)
    
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
        
    adventure_choice = input("Which adventure do you choose? (space/ocean/jungle/random) ").lower()
    
    if adventure_choice == "space":

        tense_list = ["past", "present", "future"]
        quantity_list = [1, 2, 3, 4, 5]
        tense = random.choice(tense_list)
        quantity = random.choice(quantity_list)

        print (f"Hello {char_name}! Welcome to the Random Space Story. Enjoy!\n")
            
        sentence1 = make_space_sentence(quantity, tense)
        sentence2 = make_short_space_sentence(quantity, tense)
        sentence3 = make_short_space_sentence(quantity, tense)
        sentence4 = make_space_sentence(quantity, tense)
        sentence5 = make_short_space_sentence(quantity, tense)
        sentence6 = make_space_sentence(quantity, tense)
        sentence7 = make_space_sentence(quantity, tense)
        sentence8 = make_short_space_sentence(quantity, tense)

        print (sentence1, sentence2, sentence3, sentence4)
        print ()
        print (sentence5, sentence6, sentence7, sentence8)

    elif adventure_choice == "ocean":
        tense_list = ["past", "present", "future"]
        quantity_list = [1, 2, 3, 4, 5]
        tense = random.choice(tense_list)
        quantity = random.choice(quantity_list)

        print (f"Hello {char_name}! Welcome to the Random Ocean Story. Enjoy!\n")
            
        sentence1 = make_ocean_sentence(quantity, tense)
        sentence2 = make_short_ocean_sentence(quantity, tense)
        sentence3 = make_short_ocean_sentence(quantity, tense)
        sentence4 = make_ocean_sentence(quantity, tense)
        sentence5 = make_short_ocean_sentence(quantity, tense)
        sentence6 = make_ocean_sentence(quantity, tense)
        sentence7 = make_ocean_sentence(quantity, tense)
        sentence8 = make_short_ocean_sentence(quantity, tense)

        print (sentence1, sentence2, sentence3, sentence4)
        print ()
        print (sentence5, sentence6, sentence7, sentence8)

    elif adventure_choice == "jungle":
        tense_list = ["past", "present", "future"]
        quantity_list = [1, 2, 3, 4, 5]
        tense = random.choice(tense_list)
        quantity = random.choice(quantity_list)

        print (f"Hello {char_name}! Welcome to the Random Jungle Story. Enjoy!\n")
            
        sentence1 = make_jungle_sentence(quantity, tense)
        sentence2 = make_short_jungle_sentence(quantity, tense)
        sentence3 = make_short_jungle_sentence(quantity, tense)
        sentence4 = make_jungle_sentence(quantity, tense)
        sentence5 = make_short_jungle_sentence(quantity, tense)
        sentence6 = make_jungle_sentence(quantity, tense)
        sentence7 = make_jungle_sentence(quantity, tense)
        sentence8 = make_short_jungle_sentence(quantity, tense)

        print (sentence1, sentence2, sentence3, sentence4)
        print ()
        print (sentence5, sentence6, sentence7, sentence8)   

    elif adventure_choice == "random":
        adventure = random.choice(adventures_list).lower()
        tense_list = ["past", "present", "future"]
        quantity_list = [1, 2, 3, 4, 5]
        tense = random.choice(tense_list)
        quantity = random.choice(quantity_list)

        if adventure == "space adventure":
            print (f"Hello {char_name}! Welcome to the Random Space Story. Enjoy!\n")
            
            sentence1 = make_space_sentence(quantity, tense)
            sentence2 = make_short_space_sentence(quantity, tense)
            sentence3 = make_short_space_sentence(quantity, tense)
            sentence4 = make_space_sentence(quantity, tense)
            sentence5 = make_short_space_sentence(quantity, tense)
            sentence6 = make_space_sentence(quantity, tense)
            sentence7 = make_space_sentence(quantity, tense)
            sentence8 = make_short_space_sentence(quantity, tense)

            print (sentence1, sentence2, sentence3, sentence4)
            print ()
            print (sentence5, sentence6, sentence7, sentence8)

        elif adventure == "ocean adventure":
            print (f"Hello {char_name}! Welcome to the Random Ocean Story. Enjoy!\n")
            
            sentence1 = make_ocean_sentence(quantity, tense)
            sentence2 = make_short_ocean_sentence(quantity, tense)
            sentence3 = make_short_ocean_sentence(quantity, tense)
            sentence4 = make_ocean_sentence(quantity, tense)
            sentence5 = make_short_ocean_sentence(quantity, tense)
            sentence6 = make_ocean_sentence(quantity, tense)
            sentence7 = make_ocean_sentence(quantity, tense)
            sentence8 = make_short_ocean_sentence(quantity, tense)

            print (sentence1, sentence2, sentence3, sentence4)
            print ()
            print (sentence5, sentence6, sentence7, sentence8)

        elif adventure == "jungle adventure":
            print (f"Hello {char_name}! Welcome to the Random Jungle Story. Enjoy!\n")
            
            sentence1 = make_jungle_sentence(quantity, tense)
            sentence2 = make_short_jungle_sentence(quantity, tense)
            sentence3 = make_short_jungle_sentence(quantity, tense)
            sentence4 = make_jungle_sentence(quantity, tense)
            sentence5 = make_short_jungle_sentence(quantity, tense)
            sentence6 = make_jungle_sentence(quantity, tense)
            sentence7 = make_jungle_sentence(quantity, tense)
            sentence8 = make_short_jungle_sentence(quantity, tense)

            print (sentence1, sentence2, sentence3, sentence4)
            print ()
            print (sentence5, sentence6, sentence7, sentence8)

        elif adventure == "random adventure":
            print (f"Hello {char_name}! Welcome to the Completely Random Story. Enjoy!\n")
            
            sentence1 = make_jungle_sentence(quantity, tense)
            sentence2 = make_short_space_sentence(quantity, tense)
            sentence3 = make_short_ocean_sentence(quantity, tense)
            sentence4 = make_space_sentence(quantity, tense)
            sentence5 = make_short_jungle_sentence(quantity, tense)
            sentence6 = make_ocean_sentence(quantity, tense)
            sentence7 = make_jungle_sentence(quantity, tense)
            sentence8 = make_short_space_sentence(quantity, tense)
            sentence9 = make_ocean_sentence(quantity, tense)

            print (sentence1, sentence2, sentence3, sentence4)
            print ()
            print (sentence5, sentence6, sentence7, sentence8, sentence9)         

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
    """Recieves a dictionary with which to find the name from a given letter
    at a specific index in that dictionary and returns the name
    Parameters:
    dictionary: the dictionary that stores character names as a value and the
    alphabet letter is the key
    Return: The character name"""

    letter = letter.upper()

    if letter in dictionary:
        character_name_list = dictionary[letter]
        character_name = character_name_list[index]

    return character_name    

def make_space_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    determiner = get_determiner(quantity).capitalize()
    noun = get_space_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase= get_space_prepositional_phrase(quantity)
    adjective = get_adjective()
    adverb = get_adverb()

    sentence = f"{determiner} {adjective} {noun} {adverb} {verb} {prepositional_phrase}."

    return sentence

def make_ocean_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    determiner = get_determiner(quantity).capitalize()
    noun = get_ocean_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase= get_ocean_prepositional_phrase(quantity)
    adjective = get_adjective()
    adverb = get_adverb()

    sentence = f"{determiner} {adjective} {noun} {adverb} {verb} {prepositional_phrase}."

    return sentence

def make_jungle_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    determiner = get_determiner(quantity).capitalize()
    noun = get_jungle_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase= get_jungle_prepositional_phrase(quantity)
    adjective = get_adjective()
    adverb = get_adverb()

    sentence = f"{determiner} {adjective} {noun} {adverb} {verb} {prepositional_phrase}."

    return sentence

def make_short_space_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    determiner = get_determiner(quantity).capitalize()
    noun = get_space_noun(quantity)
    verb = get_verb(quantity, tense)
    adjective = get_adjective()
    adverb = get_adverb()

    sentence = f"{determiner} {adjective} {noun} {adverb} {verb}."

    return sentence

def make_short_ocean_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    determiner = get_determiner(quantity).capitalize()
    noun = get_ocean_noun(quantity)
    verb = get_verb(quantity, tense)
    adjective = get_adjective()
    adverb = get_adverb()

    sentence = f"{determiner} {adjective} {noun} {adverb} {verb}."

    return sentence

def make_short_jungle_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    determiner = get_determiner(quantity).capitalize()
    noun = get_jungle_noun(quantity)
    verb = get_verb(quantity, tense)
    adjective = get_adjective()
    adverb = get_adverb()

    sentence = f"{determiner} {adjective} {noun} {adverb} {verb}."

    return sentence

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

def get_space_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these nine single nouns:
        "alien", "comet", "space junk", "space dog", 
        "astronaut", "Rocket", "Groot", "C3PO", "R2D2"
    Otherwise, this function will return one of
    these eight plural nouns:
        "aliens", "comets", "rockets", "space dogs", "astronauts",
        "Guardians of the Galaxy", "droids", "Storm Troopers"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
        """
    
    single_nouns = ["alien", "comet", "space junk", "space dog", 
        "astronaut", "Rocket", "Groot", "C3PO", "R2D2"]
    plural_nouns = ["aliens", "comets", "rockets", "space dogs", "astronauts",
        "Guardians of the Galaxy", "droids", "Storm Troopers"]
    
    if quantity == 1:
        noun = random.choice(single_nouns)
    elif quantity != 1:
        noun = random.choice(plural_nouns)

    return noun
    
def get_ocean_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these seven single nouns:
        "great white shark", "giant squid", "sperm whale", 
        "pufferfish", "scuba diver", "submarine", "orca"
    Otherwise, this function will return one of
    these seven plural nouns:
        "great white sharks", "giant squids", "sperm whales",
        "pufferfish", "scuba divers", "submarines", "orcas"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
        """
    
    single_nouns = ["great white shark", "giant squid", "sperm whale", 
        "pufferfish", "scuba diver", "submarine", "orca"]
    plural_nouns = ["great white sharks", "giant squids", "sperm whales",
        "pufferfish", "scuba divers", "submarines", "orcas"]
    
    if quantity == 1:
        noun = random.choice(single_nouns)
    elif quantity != 1:
        noun = random.choice(plural_nouns)

    return noun

def get_jungle_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these seven single nouns:
        "macaw", "jaguar", "mosquito", "monkey",
        "feral child", "jungle vine", "man eating plant"
    Otherwise, this function will return one of
    these seven plural nouns:
        "macaws", "jaguars", "mosquitoes", "monkeys",
        "feral children", "jungle vines", "man eating plants"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
        """
    
    single_nouns = ["macaw", "jaguar", "mosquito", "monkey",
        "feral child", "jungle vine", "man eating plant"]
    plural_nouns = ["macaws", "jaguars", "mosquitoes", "monkeys",
        "feral children", "jungle vines", "man eating plants"]
    
    if quantity == 1:
        noun = random.choice(single_nouns)
    elif quantity != 1:
        noun = random.choice(plural_nouns)

    return noun
    
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

def get_space_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_space_noun(quantity)

    prepositional_phrase = f"{preposition} {determiner} {noun}"

    return prepositional_phrase

def get_ocean_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_ocean_noun(quantity)

    prepositional_phrase = f"{preposition} {determiner} {noun}"

    return prepositional_phrase

def get_jungle_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_jungle_noun(quantity)

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
        "consistently", "curiously", "eagerly", "humourously",
        "quietly", "seriously", "succesfully", "tactfully"
    Return: a randomly chosen adverb
    """

    adverbs = ["actively", "aggressively", "assertively", "boldly",
        "consistently", "curiously", "eagerly", "humourously",
        "quietly", "seriously", "succesfully", "tactfully"]
    
    adverb = random.choice(adverbs)
    
    return adverb


if __name__ == "__main__":
    main()  
