sentence = input("Enter your word or sentence:\n")
words = sentence.split()
# print(words, type(words))
    
def count_word_frequency(words):
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word]=1
    return word_frequency

word_frequency = count_word_frequency(words)

for x, y in word_frequency.items():
    print(f"{x} : {y}")