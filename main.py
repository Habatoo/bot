from bot_files import bot
from config import Config
import nltk

nltk.download('popular', quiet=True) # for downloading packages
# uncomment the following only the first time
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only

test_config = Config()
bot.Bot(test_config.CORPUS).start_bot()

