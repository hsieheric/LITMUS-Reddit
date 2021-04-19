# Temporary python file. Will be replaced by NLP frozen model.

import sys
import tensorflow as tf
from tensorflow.keras.models import Sequential, save_model, load_model
import keras
import pandas as pd
import numpy as np
import re

from sklearn.model_selection import train_test_split

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


def normalize_text(s):
    s = s.lower()
    # remove punctuation that is not word-internal (e.g., hyphens, apostrophes)
    s = re.sub('\s\W',' ',s)
    s = re.sub('\W\s',' ',s)
    # make sure we didn't introduce any double spaces
    s = re.sub('\s+',' ',s)
    return s

def main(args):

	# Getting the right tokenizer
	data = pd.read_csv("../post_data_full.csv")
	data = data.drop(columns=['url', 'subreddit', 'score', 'permalink','Source'])
	data['text'] = [normalize_text(s) for s in data['title']]
	sentences_train, sentences_test, classes_train, classes_test = train_test_split(
	    data['text'], data['class'], test_size=0.2, random_state=1000)

	tokenizer = Tokenizer(num_words=5000)
	tokenizer.fit_on_texts(sentences_train)
	vocab_size = len(tokenizer.word_index) + 1

	input_str = " ".join(args[1:])
	input_str = pd.Series(normalize_text(input_str))

	maxlen = 50

	test_tok = tokenizer.texts_to_sequences(input_str)
	test_tok = pad_sequences(test_tok, padding='post', maxlen=maxlen)

	model = keras.models.load_model('../saved_model')

	output = model.predict(test_tok)
	print(1 if output > 0.5 else 0)

if __name__ == "__main__":
    main(sys.argv)