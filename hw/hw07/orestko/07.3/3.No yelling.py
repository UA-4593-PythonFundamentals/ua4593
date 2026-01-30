def filter_words(st):
    words = st.split()
    cleaned = ' '.join(words)
    return cleaned.capitalize()

s = "hello world"
print(filter_words(s)) 