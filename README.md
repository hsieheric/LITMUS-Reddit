# LITMUS - Reddit
This project was done by Eric Hsieh and Dongsuk Lim for Spring 2021 CS6365 - Introduction to Enterprise Computing.
The inspiration for this project came from the original [LITMUS](https://github.com/aibek76/litmus-experiments), as well as the corresponding [LITMUS paper](https://dl.acm.org/doi/10.1145/3374214).

The goal of this project was to classify misinformation on Reddit post titles that pertained to the COVID-19 vaccine. Data was aggregated and downloaded as a CSV, then hand-labelled as 0 (Misinformation) and 1 (Not misinformation). Various machine learning algorithms were run on the data; the best-performing model was saved and integrated with the frontend. The frontend provides user interaction with the classification, as well as gather additional data.

This project was done in Python 3. A detailed description of how to run main portions of the code is below.

---

# Data Collection
The main contribution of this project is the inclusion of Reddit posts as a potentially new source of data for LITMUS/EDNA. We collected our data using the PSAW Reddit API, which is built off of PRAW.

Imports:
`from psaw import PushshiftAPI`
`import pandas as pd`
`import datetime as dt`

This code can be run with the command `python data_collect.py`. It will automatically scrape and download Reddit posts in the specified subreddits before saving it to a CSV file, which is named `post_data_full.csv` in our project. The features are: class, title, url, subreddit, score, permalink. The initial class value set to 1 for generally good subreddits, and 0 for potentially controversial ones (CoronavirusFOS) to make hand-labelling easier. For our project, we used the class and title columns as our label and data, respectively.

# Model
The models are found in three notebooks. These are:
1. Covid_Baseline_Models.ipynb
2. Covid_Classification.ipynb
3. Covid_Classification_Word2Vec_Gensim.ipynb

These can all be run using Jupyter-Notebook or Google Colab.

### Applying Kaggle Spam Detection Model to Our Data.ipynb
