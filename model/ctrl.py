import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from utils.text_preprocessing import text_preparation
from keras.utils import pad_sequences
from keras.models import load_model
from googletrans import Translator
import pickle


class NetworkCtrl:

    __translator = Translator()

    def __init__(self):
        """
        Class constructor.

        Loads the model for sentiment analysis, tokenizer, and
        data about the maximum sequence length.
        """
        # Loading the pretrained sentiment analysis model.
        self.__model = load_model('CTRL.h5')

        # Loading the pretrained tokenizer.
        with open('tokenizer', 'rb') as handle:
            self.__tokenizer = pickle.load(handle)

        # Loading the data about the maximum sequence length.
        with open('max_seq_length.txt', 'r') as file:
            self.__max_seq_length = int(file.read())

    def tonality(self, text):
        """
        The method for determining the tonality of the text.

        :param text: Input text for analysis.
        :return: Array of probabilities for negative and positive sentiment of the text respectively.
        """
        # Translation and processing of text.
        comment = self.__translator.translate(text, dest="en").text
        comment = text_preparation(comment)

        # Convert textual comments to sequences of numbers and prepare for prediction.

        # Convert textual comments to sequences of numbers using a pretrained tokenizer.
        seq = self.__tokenizer.texts_to_sequences([comment])

        # Add extra zeros or trim the sequence to a fixed length.
        preprocessed_comment = pad_sequences(seq, maxlen=self.__max_seq_length)

        # Predict the comment class using the loaded model.
        prediction = self.__model.predict(preprocessed_comment, verbose=0)

        return prediction[0]
