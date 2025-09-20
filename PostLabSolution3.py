import random

def getWords(filename):
    words = []
    with open(filename, 'r') as f:
        for line in f:
            w = line.strip()
            if w:
                words.append(w.upper())
    return tuple(words)

articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')

def sentence():
    return nounPhrase() + " " + verbPhrase() + "."

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    number = int(input("Enter the number of sentences: "))
    for _ in range(number):
        print(sentence())

if __name__ == "__main__":
    main()
