from flask import Flask, render_template, request
from hivequery import Hivequery

app = Flask(__name__)

# Load home page
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search-tweets', methods=["GET", "POST"])
def searchtweets():

	# get user input
	date = request.form['dsearch']
	kwords = request.form['kword']
	if kwords == "":
		kword = ""
	else:
		kwords = kwords.split()
		kword = kwords[0]
	
	#build queries from user input
	t_query = twitter_query(date,kword)
	n_query = news_query(date,kword)

	# build hive object, retrieve queries from hive on hadoop cluster
	myquery = Hivequery()
	tweetsout = myquery.hive_tq(t_query)
	newsout = myquery.hive_nq(n_query)

	return render_template('index.html', tweetsout=tweetsout, newsout=newsout)

# build sql query from user input
def twitter_query(date,kword):
	if kword == "":
		query = "SELECT * FROM covid_tweets WHERE covid_tweets.post_date LIKE '%" +date+ "%' SORT BY favorites DESC LIMIT 1"
	else:
		query = "SELECT * FROM covid_tweets WHERE lower(covid_tweets.post_text) LIKE '% " +kword+ " %' SORT BY favorites DESC LIMIT 1"
	
	return query

# build sql query from user input
def news_query(date,kword):
	if kword == "":
		query = "SELECT * FROM covid_news WHERE covid_news.post_date LIKE '%" +date+ "%' LIMIT 1"
	else:
		query = "SELECT * FROM covid_news WHERE lower(covid_news.title) LIKE '% " +kword+ " %' LIMIT 1"

	return query

if __name__ == "__main__":
	app.run()
