import nltk
import re
from collections import Counter
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

#Accepts a sentence and returns a list with url(s) and the sentence 
def get_url_from_sentence(sentence):
    count = sentence.count('https')
    urls = []
    if(count == 0):
        return [sentence, '']
    else:
        while(count>0): 
            startIdx = sentence.find('https', 0, len(sentence)-1)
            char = sentence[startIdx-1]
            if(char == '[' or char == '(' or char == ' '):
                if(char == '['):
                    stopChar = ']'
                elif(char == '('):
                    stopChar = ')'
                else:
                    stopChar = char

            stopIdx = sentence.find(stopChar, startIdx)
            urls.append(sentence[startIdx:stopIdx])
            sentence = sentence[:startIdx-1] + ' ' + sentence[stopIdx+1:]
            count -= 1

        return [sentence, urls]

def get_reduced_data(data):
    collection =  Counter(data)
    reducedData = {}
    junkWords = ["a", "and", "at", "but", "each", "i", "if", "id", "ill", "im", 
                "in", "it", "cs", "want", "wants", "the", "there", "these", "this",
                "also", "another", "article", "background", "makes", "many", "may",
                "mentioned", "might", "study", "subject", "super", "sure", "question",
                "program", "programs", "doesnt", "dont", "eg", "isnt", "kind", "know",
                "able", "along", "already", "answer", "basic", "basically", "called", 
                "cant", "cause", "better", "believe", "even", "exactly", "explain",
                "find", "follow", "etc", "get", "give", "go", "goes", "video", "way",
                "would", "youre", "ways", "could", "degree", "enough", "essentially",
                "help", "huge", "like", "maybe", "means", "much", "need", "really", "said",
                "see", "think", "though", "well", "since", "lot", "make", "whatever", "try"
                "talk", "book", "something", "try"]
    for key in collection:
        key = key.lower()
        if(collection[key]>3 and key not in junkWords):
           reducedData[key] = collection[key]
    
    return sorted((reducedData))

def get_sentences_from_data(data, words):
    sentencesList = []
    sentences = nltk.sent_tokenize(data)

    for sentence in sentences:
        sentence, urls = get_url_from_sentence(sentence)
        sentence = re.sub('[^A-Za-z0-9 ]+', '', sentence)

        if any(word in sentence for word in words):
            if sentence not in sentencesList:
                sentencesList.append(sentence)
    
    return sentencesList

def natural_language_processing(text): 
    textList = []
    urlsList = []

    lemmatizer = WordNetLemmatizer()
    sentences = nltk.sent_tokenize(text)

    for sentence in sentences:
        sentence, urls = get_url_from_sentence(sentence) #Get a list of the modified sentence and a list or urls

        #Iterate through the list and append each url string to urlsList
        for url in urls:
            urlsList.append(url)

        #Regex to replace anything that is not Uppercase/Lowecase character, digit, or " " with empty char('')
        sentence = re.sub('[^A-Za-z0-9 ]+', '', sentence)
        
        #tokenize each sentence into words
        words = nltk.word_tokenize(sentence)

        for word in words:
            lemmatizer.lemmatize(word, map_pos_to_word(word))
            textList.append(word)

    #Remove stopwords:
    stopWords = set(stopwords.words("english"))
    textList = [word for word in textList if word not in stopWords]

    urlsList = list(filter(None, urlsList))

    return [textList, urlsList]


def main():
    filename = "/Users/theonlyroy/Desktop/Parse Reddit Comments/reddit_comments.txt"
    text = get_text_from_file(filename)
    data, urls = natural_language_processing(text)

    reduced_data = get_reduced_data(data)

    info = get_sentences_from_data(text, reduced_data)

    f = open("/Users/theonlyroy/Desktop/bio.txt", "w+")

    f.write("User Comments:\n\n")
    for line in info:
        f.write(line+"\n")
    
    f.write("\nURLs:\n\n")
    for url in urls:
        f.write(url+"\n")
    
    f.close()

if __name__ == "__main__":
    main()