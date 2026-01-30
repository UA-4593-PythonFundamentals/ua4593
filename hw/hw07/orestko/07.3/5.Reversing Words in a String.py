def reverse_words(sentence):
    words = sentence.strip().split()
    return ' '.join(words[::-1])


print(reverse_words("Hello World")) 
print(reverse_words("Hi There."))  