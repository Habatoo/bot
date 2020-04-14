import pandas as pd
import pickle
from bot_files import make_data


class Config:
    CORPUS = open(
            './data/dialogues.txt', 'r', encoding='utf8', errors='ignore')
    DATAFRAME = pd.read_csv('./data/df.csv', nrows=5000)
    DATAFRAME.dropna(inplace=True)
    DATAFRAME_TFIDF = pd.read_csv('./data/df_tfidf.csv')

    with open('./data/stop_words.pkl', 'rb') as f:
        STOPWORDS = pickle.load(f)
    with open('./data/model.pkl', 'rb') as f:
        MODEL = pickle.load(f)


if __name__ == '__main__':
    test_cinfig = Config()
    print(test_cinfig.DATAFRAME.shape)
    print(test_cinfig.DATAFRAME_TFIDF.shape)
