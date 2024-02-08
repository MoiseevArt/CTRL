from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import re

nltk.download('stopwords', quiet=True)
# Set of English stop words.

stop_words = set(stopwords.words('english'))


def text_preparation(text):
    """
    Function for text preprocessing.

    :param text: Input text for preprocessing.
    :return: Preprocessed text.
    """
    if isinstance(text, str):
        # Remove links, hashtags, English letters, and words starting with '@'.
        text = re.sub(r'http\S+|#[\w_]+|@\w+|[^\w\s]', ' ', text)

        tokens = word_tokenize(text)

        # Remove stop words and then join the tokens into a string.
        text = [word for word in tokens if word.lower() not in stop_words]
        text = ' '.join(text)

        return text.lower()
    else:
        return text
