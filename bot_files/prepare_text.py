import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer # to perform tfidf
import pandas as pd
import re
from nltk.stem import wordnet
from nltk import pos_tag
from sklearn.metrics import pairwise_distances # to perfrom cosine similarity


class Text_prep:
    """
    Theme text
    """
    def __init__(self, stopwords):
        # using tf-idf
        self.stopwords = stopwords

    def text_normalization(self, text):
        # function that performs text normalization steps
        text = str(text).lower() # text to lower case
        spl_char_text=re.sub(r'[^ а-яА-ЯёЁ]', '', text) # removing special characters
        tokens = nltk.word_tokenize(spl_char_text) # word tokenizing
        lema = wordnet.WordNetLemmatizer() # intializing lemmatization
        tags_list = pos_tag(tokens, tagset=None) # parts of speech
        lema_words = []   # empty list 
        for token, pos_token in tags_list:
            if token in self.stopwords:
                continue
            if pos_token.startswith('V'):  # Verb
                pos_val = 'v'
            elif pos_token.startswith('J'): # Adjective
                pos_val = 'a'
            elif pos_token.startswith('R'): # Adverb
                pos_val = 'r'
            else:
                pos_val = 'n' # Noun
            lema_token = lema.lemmatize(token, pos_val) # performing lemmatization
            lema_words.append(lema_token) # appending the lemmatized token into a list
        return " ".join(lema_words) # returns the lemmatized tokens as a sentence

    def response(self, df_tfidf, user_response, model):
        # defining a function that returns response to query using tf-idf
        lemma = self.text_normalization(user_response) # calling the function to perform text normalization
        print('lemma', lemma)
        tf = model.fit_transform([lemma]).toarray() # applying tf-idf
        print(tf.shape)
        print(df_tfidf.shape)
        cos = 1 - pairwise_distances(df_tfidf, tf, metric='cosine') # applying cosine similarity
        index_value = cos.argmax() # getting index value 
        return self.df['Response'].loc[index_value]

