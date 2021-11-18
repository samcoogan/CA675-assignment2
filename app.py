from flask import Flask, render_template, request
from hivequery import Hivequery

app = Flask(__name__)

# Load home page
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search-tweets', methods=["GET", "POST"])
def searchtweets():

	date = request.form['dsearch']
	location = request.form['location']
	kwords = request.form['kword']
	kwords = kwords.split("")
	kword = kwords[0]
	t_query = twitter_query(date,location,kword)
	n_query = news_query(date,location)
	
	#print(tweetsout)
	#print(newsout)


	myquery = Hivequery()
	#q1 = "SELECT * FROM covid_tweets SORT BY favorites DESC LIMIT 1"
	tweetsout = myquery.hive_q(t_query)
	#newsout = q1
	#print(data)

	#return jsonify(tweetsout)
	return render_template('index.html', tweetsout=t_query, newsout=n_query)


def twitter_query(date,location,kword):
	if kword == "" and location == "world":
		query = "SELECT post_text FROM covid_tweets WHERE post_date EQUALS " +date+ " SORT BY favorites DESC LIMIT 1"
	elif kword == "":
		query = "SELECT post_text FROM covid_tweets WHERE post_date EQUALS " +date+ " AND lower(location) like '%'" +location+ "'%' SORT BY favorites DESC LIMIT 1"
	elif location == "world":
		query = "SELECT post_text FROM covid_tweets WHERE post_date EQUALS " +date+ " AND post_text LIKE '%" +kword+ "%' SORT BY favorites DESC LIMIT 1"
	else:
		query = "SELECT post_text FROM covid_tweets WHERE post_date EQUALS " +date+ " AND lower(location) like '%'" +location+ "'%' AND post_text LIKE '%" +kword+ "%' SORT BY favorites DESC LIMIT 1"
	
	return query

def news_query(date,location):
	if location == "world":
		query = "SELECT headline FROM news_headlines WHERE post_date EQUALS " +date+ " SORT BY ranking DESC 1"
	else:
		query = "SELECT headline FROM news_headlines WHERE post_date EQUALS " +date+ " AND lower(location) EQUALS " +location+ " SORT BY ranking DESC 1"

	return query

if __name__ == "__main__":
	app.run()
