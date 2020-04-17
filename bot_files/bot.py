import warnings
import random
warnings.filterwarnings('ignore')
from bot_files import prepare_text


class Bot:
    # Keyword Matching
    GREETING_INPUTS = ("привет", "здравствуй", "здорово", "здаров", "хай", "всем привет",)
    GREETING_RESPONSES = ["привет", "здравствуй", "здорово", "здаров", "хай"]

    def __init__(self, df, df_tfidf, stopwords, model):
        self.df = df
        self.stopwords = stopwords
        self.df_tfidf = df_tfidf
        self.model = model
        self.user_text = prepare_text.Text_prep(self.stopwords)

    def start_bot(self):
        def greeting(sentence):
            """If user's input is a greeting, return a greeting response"""
            for word in sentence.split():
                if word.lower() in Bot.GREETING_INPUTS:
                    return random.choice(Bot.GREETING_RESPONSES)
        flag = True
        print("Бот: Я Бот. Пиши вопрос, я отвечу. Если хочешь уйти, пиши пока!")
        while flag == True:
            print("User: ", end="")
            user_response = input().lower()
            if user_response != 'пока':
                if user_response == 'спасибо' or user_response == 'спсб':
                    flag = False
                    print("Бот: всегда пожалуйста...")
                else:
                    if greeting(user_response) != None:
                        print("Бот: " + greeting(user_response))
                    else:
                        print("Бот: ", end="")
                        try:
                            print(self.user_text.response(
                                self.df, self.df_tfidf, user_response, self.model))
                        except:
                            print(self.user_text.model_answ(user_response, self.model))
            else:
                flag = False
                print("Бот: Пока! Увидимся...")
