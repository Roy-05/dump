import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords

def map_pos_to_word(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()

    #Map POS code to accepted format
    tag_dict = {
        "J": wordnet.ADJ,
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "R": wordnet.ADV
    } 

    return tag_dict.get(tag, wordnet.NOUN)

def get_text_from_file(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()

    return text

def natural_language_processing(text):
    lemmatizer = WordNetLemmatizer()
    sentences = nltk.sent_tokenize(text)
    textList = []

    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        for word in words:
            lemmatizer.lemmatize(word, map_pos_to_word(word))
            textList.append(word)

    #Remove stopwords:
    stopWords = set(stopwords.words("english"))
    textList = [word for word in textList if word not in stopWords]

    print(textList)
    
def main():
    filename = "/Users/theonlyroy/Desktop/Parse Reddit Comments/reddit_comments.txt"
    text = get_text_from_file(filename)

    natural_language_processing(text)


if __name__ == "__main__":
    main()