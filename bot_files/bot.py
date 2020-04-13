import warnings
import random
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
warnings.filterwarnings('ignore')
from bot_files import prepare_text

import nltk
from nltk.stem import WordNetLemmatizer

class Bot:
    # Keyword Matching
    GREETING_INPUTS = ("привет", "здравствуй", "здорово", "здаров", "хай", "всем привет",)
    GREETING_RESPONSES = ["привет", "здравствуй", "здорово", "здаров", "хай"]

    def __init__(self, df_tfidf, stopwords, model):
        self.stopwords = stopwords
        self.df_tfidf = df_tfidf
        self.model = model

    def start_bot(self):
        user_text = prepare_text.Text_prep(self.stopwords)

        def greeting(sentence):
            """If user's input is a greeting, return a greeting response"""
            for word in sentence.split():
                if word.lower() in Bot.GREETING_INPUTS:
                    return random.choice(Bot.GREETING_RESPONSES)

        flag=True
        print("Бот: Я Бот. Я могу говорить. Если хочешь уйти, пиши пока!")
        while (flag==True):
            user_response = "User: " + input()
            user_response=user_response.lower()
            if (user_response!='пока'):
                if (user_response=='спасибо' or user_response=='спсб'):
                    flag=False
                    print("Бот: всегда пожалуйста...")
                    break
                else:
                    if(greeting(user_response) != None):
                        print("Бот: " + greeting(user_response))
                    else:
                        print("Бот: ",end="")
                        print(user_text.response(self.df_tfidf, user_response, self.model))
            else:
                flag=False
                print("Бот: Пока! Увидимся...")
