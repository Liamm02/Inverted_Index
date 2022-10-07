import string
from nltk.corpus import stopwords


def Translator(file):
    """This function gets rid of all the punctuations and special characters,
    it also converts the document to lowercase"""
    translator = str.maketrans(dict.fromkeys(string.punctuation, ' '))

    # Convert the entire document to lower case to not have duplicate words
    f = file.translate(translator).lower()
    special = ["×", "·", "”", "“", "—", "«", "»", "—", "º", "ª", "π", '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%',
               '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '¿', '¡', '#',
               '$', ')', '/']

    for character in special:
        f = f.replace(character, "")
    return f

def StopWords_deleter(text):

    stopWords = set(stopwords.words('spanish')) | set(stopwords.words('english'))

    # Now we create the dictionary that stores all the words and a list with the lines it appears in
    d = {}
    for num, line in enumerate(text):
        for word in line.split(" "):
            if word != "":
                if word in stopWords:
                    continue
                else:
                    if word in d:
                        d[word].append(num + 1)
                    if word not in d:
                        d[word] = [num + 1]
    return d