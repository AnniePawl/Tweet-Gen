with open('sample_text.tx') as f:
    text = f.read()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~”“’'''
    no_punctuation = ""

    for character in text:
        if character not in punctuations:
            no_punctuation = no_punctuation + character

    no_punctuation.lower()

    formatted_words_array = no_punctuation.split()
