import warnings
import random
warnings.filterwarnings('ignore')
from bot_files import prepare_text, voice_totext


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

        def input_change(voice):
            if voice:
                return voice_totext.assistant(voice_totext.myCommand())
            return input().lower()

        flag = True
        voice = False
        print("Bot: Я Бот. Пиши вопрос, я отвечу. Если хочешь уйти, пиши пока!")
        print("Bot: Могу отвечать на голос - пиши 'голос'. Если хочешь опять писать, скажи 'стоп голос'")
        while flag == True:
            print("User: ", end="")
            user_response = input_change(voice)
            if user_response == 'голос':
                voice = True
                continue
            if user_response == 'стоп голос':
                voice = False
                continue 
            if user_response == 'спасибо' or user_response == 'спсб':
                print("Bot: всегда пожалуйста...")
                continue
            elif user_response != 'пока':
                if greeting(user_response) != None:
                    print("Bot: " + greeting(user_response))
                else:
                    print("Bot: ", end="")
                    try:
                        print(self.user_text.response(
                            self.df, self.df_tfidf, user_response, self.model))
                    except:
                        print(self.user_text.model_answ(user_response, self.model_2))
            else:
                flag = False
                print("Bot: Пока! Увидимся...")
