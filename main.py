from bot_files import bot, prepare_text
from config import Config

# import nltk
# nltk.download('popular', quiet=True) # for downloading packages
# uncomment the following only the first time
# nltk.download('punkt') # first-time use only
# nltk.download('wordnet') # first-time use only
# nltk.download('stopwords')

text_dialog = Config()
# text_list = text_dialog.CORPUS.readlines()
stopwords = text_dialog.STOPWORDS
df = text_dialog.DATAFRAME
df_tfidf = text_dialog.DATAFRAME_TFIDF
model = text_dialog.MODEL

text_prep = prepare_text.Text_prep(stopwords)
# print('norm', text_prep.text_normalization('Ты кто?'))
# print(text_prep.response(df, df_tfidf, 'Ты кто?', model))

bot.Bot(df, df_tfidf, stopwords, model).start_bot()
