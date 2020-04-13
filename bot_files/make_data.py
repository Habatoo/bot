import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class Make_Df:
    def __init__(self, text_list=None):
        self.text_list = text_list

    def make_df(self):
        """
        Make DataFrame - Phrase: Response
        """
        phrase = []  # Phrase
        response = []  # Response
        temp = []
        dialog_data = {'Phrase': phrase, 'Response': response}
        for sentence in self.text_list:
            if sentence != '\n':
                temp.append(sentence)
            else:
                for num_sentence in range(len(temp) - 1):
                    phrase.append(temp[num_sentence].strip())
                    response.append(temp[num_sentence + 1].strip())
                temp = []
        return pd.DataFrame(dialog_data).drop_duplicates()

    def make_df_tfidf(self, df):
        tfidf = TfidfVectorizer()
        x_tfidf = tfidf.fit_transform(df['Lemmatized_text']).toarray()
        df_tfidf = pd.DataFrame(
                x_tfidf, columns=tfidf.get_feature_names())
        return df_tfidf, tfidf
