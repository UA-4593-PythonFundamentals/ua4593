def filter_words(st):
    st = " ".join(st.split())

    return st[:1].upper() + st[1:].lower()

