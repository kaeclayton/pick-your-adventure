# Pick Your Adventure

A text adventure game in Python that builds a new random story every time you play. Choose a character, pick a space, ocean, or jungle adventure (or let the game surprise you), and read a story made from randomly chosen words and phrases.

## How to play

You need Python 3. From the project folder, run:

```
python pick_your_adventure.py
```

The game asks you to:

1. Choose a male or female character
2. Pick a letter from A to Z to get your character's name
3. Choose an adventure: `space`, `ocean`, `jungle`, or `random`

After each story, you can play again with the same character or choose a new one.

## Sample story

```
Hello Karen Koolidge! Welcome to the Random Jungle Story. Enjoy!

A likeable monkey quietly will growl over this man eating plant. That miniature
macaw tactfully will break. A lazy jaguar assertively will fight. The confident
man eating plant humorously will run onto the man eating plant.
```

## Running the tests

The tests use [pytest](https://pytest.org). Install it once with `pip install pytest`, then run:

```
pytest test_pick_your_adventure.py
```

## Project history

This game started as my final project for CSE 111 (Programming with Functions) at BYU-Pathway Worldwide. I later came back to it to improve the code:

- **Input validation:** a reusable `ask_choice` function re-asks any question until the answer is valid, so the game no longer crashes on unexpected input.
- **Restructuring:** the space, ocean, and jungle stories each had their own copy of the same functions. They now share one set of functions with the word lists stored in a dictionary, which cut the program from 624 to about 380 lines.
- **Play again:** a loop lets you play more stories and keep or change your character.
- **Tests:** pytest tests for the name lookup, file loading, word choice, and sentence building.
- **Bug fixes:** missing commas in word lists, sentence spacing, doubled periods, and a crash when the names file is missing.

The commit history shows each of these changes step by step.

## Files

- `pick_your_adventure.py`: the game
- `character_name.csv`: the character names for each letter
- `test_pick_your_adventure.py`: the tests
