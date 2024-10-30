import random

jokes = []
class Joke:
    def __init__(self):
        self.question = ""
        self.answer = ""

def read_jokes():
    with open("DadJokes.txt", "r") as f:
        for line in f:
            readline = line
            jokes.append(readline)
    print (jokes)

read_jokes()
