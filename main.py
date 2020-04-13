from bot_files import bot
from bot_files import make_data
from config import Config

# import nltk
# nltk.download('popular', quiet=True) # for downloading packages
# uncomment the following only the first time
# nltk.download('punkt') # first-time use only
# nltk.download('wordnet') # first-time use only
# nltk.download('stopwords')

text_dialog = Config()
text_list = text_dialog.CORPUS.readlines()
stopwords = text_dialog.STOPWORDS
df = text_dialog.DATAFRAME
df_tfidf = text_dialog.DATAFRAME_TFIDF
model = text_dialog.MODEL
bot.Bot(df_tfidf, stopwords, model).start_bot()
