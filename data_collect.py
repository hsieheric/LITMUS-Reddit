from psaw import PushshiftAPI
import pandas as pd
import datetime as dt

api = PushshiftAPI()
start_epoch=int(dt.datetime(2020, 12, 1).timestamp())

api_request_generator = api.search_comments(q='vaccine', subreddit='coronavirus', score='<0',
	filter = ['url', 'author', 'title', 'body', 'score', 'permalink', ], limit = 1000)
temp = pd.DataFrame([comment.d_ for comment in api_request_generator])

temp.to_csv('coronavirus_comments.csv')