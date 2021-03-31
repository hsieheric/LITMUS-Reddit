from psaw import PushshiftAPI
import pandas as pd
import datetime as dt

api = PushshiftAPI()
# start_epoch=int(dt.datetime(2020, 12, 1).timestamp())


# Comments

# api_request_generator = api.search_comments(q='vaccine', subreddit='coronavirus', score='<0',
# 	filter = ['url', 'author', 'title', 'body', 'score', 'permalink', ], limit = 10000)
# temp = pd.DataFrame([comment.d_ for comment in api_request_generator])

# temp.to_csv('coronavirus_comments.csv')




# Posts

def get_posts():
	subreddits = ['coronavirus', 'COVID19', 'CoronavirusNewYork']
	posts = None
	for i in subreddits:
		pos_api_request_generator = api.search_submissions(q='vaccine', subreddit=i, score='>3', filter = ['url', 'subreddit', 'title', 'score', 'permalink'], sort = 'desc')
		pos_df = pd.DataFrame([comment.d_ for comment in pos_api_request_generator])
		pos_df['class'] = pd.Series([1 for x in range(len(pos_df.index))], index=pos_df.index)

		neg_api_request_generator = api.search_submissions(q='vaccine', subreddit=i, score='<1', filter = ['url', 'subreddit', 'title', 'score', 'permalink'], sort = 'asc')
		neg_df = pd.DataFrame([comment.d_ for comment in neg_api_request_generator])
		neg_df['class'] = pd.Series([0 for x in range(len(neg_df.index))], index=neg_df.index)

		posts = pd.concat([posts, pos_df, neg_df])

	fos_api_request_generator = api.search_submissions(q='vaccine', subreddit='coronavirusFOS', filter = ['url', 'subreddit', 'title', 'score', 'permalink'], sort = 'desc')
	fos_df = pd.DataFrame([comment.d_ for comment in fos_api_request_generator])
	fos_df['class'] = pd.Series([0 for x in range(len(fos_df.index))], index=fos_df.index)

	posts = pd.concat([posts, fos_df])

	cols = ['class', 'title', 'url', 'subreddit', 'score', 'permalink']
	posts = posts[cols]
	posts.to_csv('post_data_full.csv', index = False, encoding='utf-8-sig')
	cols = ['class', 'title']
	posts = posts[cols]
	posts.to_csv('post_data.csv', index = False, encoding='utf-8-sig')

if __name__ == "__main__":
	get_posts()
