import random
def choose_word(hard_mode:bool = False) -> str:
    file= "data/allowed_words.txt" if hard_mode else "data/words.txt"
    with open(file, 'r') as word_file:
        choice = random.choice(word_file.read().split(","))
        return choice


def is_allowed(word : str) -> bool:
    with open("data/allowed_words.txt", 'r') as word_file:
        allowed = word.lower() in word_file.read().split(",")
        return allowed

def choose_praise() -> str:
        pass