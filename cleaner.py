with open('hitchhikers.txt') as f:
    text = f.read()
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~”“’'''
    no_punctuation = ""

    for character in text:
        if character not in punctuation:
            no_punctuation = no_punctuation + character

    no_punctuation.lower()

    formatted_words_array = no_punctuation.split()

print(formatted_words_array)
