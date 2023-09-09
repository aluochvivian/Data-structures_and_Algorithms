# Define a function to calculate word frequency in a sentence
def word_frequency(sentence):
    words = sentence.lower().split()
    word_count = {}

    for word in words:
        word = word.strip('.,!?')
        if word:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count
