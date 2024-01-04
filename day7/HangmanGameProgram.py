import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words = [
    "giraffe", "penguin", "armadillo", "chimpanzee", "salamander", "platypus",
    "kangaroo", "orangutan", "rhinoceros", "hummingbird",

    
    "spaghetti", "broccoli", "avocado", "chocolate", "pineapple", "hamburger",
    "lasagna", "croissant", "burrito", "cheesecake",

    "Egypt", "Australia", "Antarctica", "Brazil", "Canada", "Italy", "Germany",
    "Japan", "Greece", "Scotland",

    
    "computer", "telescope", "bicycle", "trumpet", "camera", "umbrella",
    "skateboard", "paintbrush", "headphones", "flashlight",

    "dancing", "singing", "swimming", "laughing", "painting", "reading", "writing",
    "cooking", "playing", "cleaning",

    "happiness", "sadness", "anger", "excitement", "surprise", "fear", "love",
    "boredom", "frustration", "confusion",


    "rainbow", "galaxy", "puzzle", "mystery", "adventure", "treasure", "superhero",
    "friendship", "imagination", "creativity"
]

chosenWord = random.choice(words)
wordLength = len(chosenWord)
print(chosenWord)
display = []
for i in range(wordLength):
    display.append('_')
print(display)
endOfGame = False
while not endOfGame:
    guessWord = input("Guess a letter:").lower()

    for position in range(wordLength):
        letter = chosenWord[position]
        if letter == guessWord:
            display[position] = letter
        
    print(display)

if "_" not in display:
    endOfGame = True
    print("You Win!")