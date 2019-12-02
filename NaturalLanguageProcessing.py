import nltk
import re
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
    print(textList)

def main():
    filename = "/Users/theonlyroy/Desktop/Parse Reddit Comments/reddit_comments.txt"
    text = get_text_from_file(filename)

    natural_language_processing(text)


if __name__ == "__main__":
    main()