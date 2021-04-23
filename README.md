# LITMUS - Reddit
This project was done by Eric Hsieh and Dongsuk Lim Spring 2021 for CS6365 - Introduction to Enterprise Computing.
The inspiration for this project came from the original [LITMUS code](https://github.com/aibek76/litmus-experiments), as well as the corresponding [LITMUS paper](https://dl.acm.org/doi/10.1145/3374214).

There are three main parts to this project: data collection, data preprocessing and classification, and a frontend webapp.

The goal of this project was to classify misinformation on Reddit post titles that pertained to the COVID-19 vaccine. Data was aggregated and downloaded as a CSV, then hand-labelled as 0 (Misinformation) and 1 (Not Misinformation). Various machine learning algorithms were run on the data; the best-performing model was saved and integrated with the frontend. The frontend provides user interaction with the classification, as well as gather additional data.

This project was done in Python 3. A detailed description of how to run main portions of the code is below. To see the main project now, run `python app.py` from the `enterprise_app` folder, making sure all packages are installed.

---

# Data Collection
The main contribution of this project is the inclusion of Reddit posts as a potentially new source of data for LITMUS/EDNA. We collected our data using the PSAW Reddit API, which is built off of PRAW.

Imports:
`from psaw import PushshiftAPI`

`import pandas as pd`

`import datetime as dt`

This code can be run with the command `python data_collect.py`. It will automatically scrape and download Reddit posts in the specified subreddits before saving it to a CSV file, which is named `post_data_full.csv` in our project. The features are: class, title, url, subreddit, score, permalink. The initial class value set to 1 for generally good subreddits, and 0 for potentially controversial ones (CoronavirusFOS) to make hand-labelling easier. For our project, we used the class and title columns as our label and data, respectively.

# Data Preprocessing and Model Classification

The preprocessing and models are found in three notebooks. These are:
1. Covid_Baseline_Models.ipynb
2. Covid_Classification.ipynb
3. Covid_Classification_Word2Vec_Gensim.ipynb

These can all be run using Jupyter-Notebook or Google Colab.

### Data Preprocessing

Data preprocessing is done through SKLearn's CountVectorizer and Keras' Tokenizer. Both of these libraries can convert text into tokens and embeddings for the machine learning algorithm to use as an input.

## Notebooks

---

### Covid_Baseline_Models.ipynb
Gaussian Naive Bayes, Logistic Regression, and K-Nearest Neighbors classification.
Packages used: `numpy, pandas, os, re, nltk, sklearn, tensorflow, keras`

### Covid_Classification.ipynb
This notebook runs our main model. It is a Keras Sequential model that uses word embeddings to encode the training data before inputting it to the model. It achieved a training accuracy of almost 100%, and a testing accuracy of almost 90%. 
Packages used: `numpy, pandas, os, sklearn, re, tensorflow, keras`

### Covid_Classification_Word2Vec_Gensim
This notebook uses the GenSim Word2Vec model that has been trained on word2vec-google-news-300 to perform pseudo-unsupervised learning. The main purpose is to create a visualization of how the model clustered our data. 
Packages used: `logging, gensim, pandas, re, nltk, sklearn, plotly, matplotlib`

# Front-End and Model Integration
The frontend is done in HTML, and is hosted on a local Flask server. In order to run the frontend, run the command `python app.py` from the `enterprise_app` folder.
Packages used: `flask, subprocess, sys, os`

The templates for the frontend display can be found in the `templates` folder in `enterprise_app`. 

Additionally, the Flask server calls a python subprocess to run the file `model_predict.py`, which uses the frozen model saved in the `LITMUS_Reddit` folder.
Packages used: `sys, tensorflow, keras, pandas, numpy, re, sklearn`

The outputs from the webapp are saved to `user_data.csv` located in the `enterprise_app` folder.