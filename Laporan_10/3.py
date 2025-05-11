def get_unique_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    tandabaca = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    translator = str.maketrans('', '', tandabaca)
    words = text.translate(translator).lower().split()

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    unique_words = [word for word, count in word_count.items() if count == 1]
    return unique_words

filename = input("Masukkan nama file teks: ")
try:
    unique_words = get_unique_words(filename)
    print("Kata-kata unik (hanya muncul sekali) dalam file:")
    for word in sorted(unique_words):
        print(word)
except FileNotFoundError:
    print("File tidak ditemukan.")
