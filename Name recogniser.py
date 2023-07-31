# Importing the required libraries
import nltk
from nltk.corpus import stopwords


# Function to extract the proper nouns

def ProperNounExtractor(text):
    print('PROPER NOUNS EXTRACTED :')
    from nltk.tokenize import word_tokenize, sent_tokenize

    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        for (word, tag) in tagged:
            if tag == 'NNP':  # If the word is a proper noun
                print(word)

text =  "ram"

# Calling the ProperNounExtractor function to extract all the proper nouns from the given text.
ProperNounExtractor(text)