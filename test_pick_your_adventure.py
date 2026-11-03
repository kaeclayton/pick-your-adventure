"""
Kae Clayton
To test the functions in pick_your_adventure.py
"""

from pick_your_adventure import get_character_name, get_name_dictionary, \
    get_noun, make_sentence, NOUNS
import pytest


def test_get_character_name():
    """Tests that get_character_name finds the right name for a letter."""
    names = {"A": ["A", "Allison Adrian", "Abram Abrahamson"]}

    assert get_character_name(names, 1, "A") == "Allison Adrian"
    assert get_character_name(names, 2, "A") == "Abram Abrahamson"
    assert get_character_name(names, 1, "a") == "Allison Adrian"

def test_get_character_name_missing_letter():
    """Tests that get_character_name returns the default name when the 
    letter is not in the dictionary."""
    names = {"A": ["A", "Allison Adrian", "Abram Abrahamson"]}

    assert get_character_name(names, 1, "Z") == "Alex Adventurer"

def test_get_name_dictionary():
    """Tests that get_name_dictionary reads all 26 letters from the CSV."""
    names = get_name_dictionary("character_name.csv", 0)

    assert len(names) == 26
    assert names["C"] == ["C", "Coco Carroway", "Caleb Caldwell"]

def test_get_name_dictionary_missing_file():
    """Tests that get_name_dictionary returns an empty dictionary when
    the file does not exist."""
    assert get_name_dictionary("no_such_file.csv", 0) == {}

def test_get_noun():
    """Tests that get_noun picks from the right theme and quantity."""
    for theme in ["space", "ocean", "jungle"]:
        assert get_noun(theme, 1) in NOUNS[theme]["single"]
        assert get_noun(theme, 3) in NOUNS[theme]["plural"]

def test_make_sentence():
    """Tests that sentences start with a capital letter and end with 
    exactly one period."""
    for with_phrase in [True, False]:
        sentence = make_sentence("ocean", 1, "past", with_phrase=with_phrase)

        assert sentence[0].isupper()
        assert sentence.endswith(".")
        assert not sentence.endswith("..")

def test_short_sentence_is_shorter():
    """Tests that a sentence with a phrase has more words than one without."""
    long_sentence = make_sentence("space", 1, "present")
    short_sentence = make_sentence("space", 1, "present", with_phrase=False)

    assert len(long_sentence.split()) > len(short_sentence.split())

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])