from flask import Flask, render_template, redirect, jsonify, url_for, request, session
from flask_restful import Api
from flask_wtf import Form
from flask_wtf.csrf import CsrfProtect
from wtforms import SelectField
import db.helper as connection


# initalize server
app = Flask(__name__, template_folder='Web/pages', static_folder='public')
api = Api(app)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
CsrfProtect(app)


# create connection object and get data for teams and players
db = connection.Connection()

@app.route('/', methods=['GET', 'POST'])
def index():
    class SelectUserForm(Form):
        users = db.get_user()
        name = SelectField(coerce=int, choices=users, default=25073877)
    form = SelectUserForm()
    print(form.errors)
    # handle post request in form
    if form.validate_on_submit():
        session['user_id'] = form.name.data #gets user selected option
        print "The USER ID is -----------------"
        print session['user_id'] #user selected input value can be used for compare
        print "The USER ID is -----------------"
        return redirect('/filter')
    return render_template("index.html", form=form)


@app.route('/filter', methods=['GET','POST'])
def filter():
    class SelectFilterForm(Form):
        user_id = session['user_id']
        filters = db.get_all()
        name = SelectField(coerce=int, choices=filters)
    form = SelectFilterForm()
    # handle post request in form
    if form.is_submitted():
        session['filter_id'] = form.name.data
        if (session['filter_id'] == None):
            session['filter_id'] = 1
        print "The FILTER ID is -----------------"
        print session['filter_id']
        print "The FILTER ID is -----------------"
        return redirect('/tables')
    print " NO FILTER ID WAS FOUND"
    return render_template("filter.html", form=form)

@app.route('/tables', methods=['GET', 'POST'])
def tables():
    filter_id = session['filter_id']
    if filter_id == 1: # "View 01: Defines method that returns a join of 3 tables"
        join = db.get_all()
        return render_template("join_tables.html", join_table=join)
    elif filter_id == 2: # "View 02: Defines method that returns the users in the database"
        user = db.get_Names()[0]
        return render_template("display_users.html", user=user[0])
    elif filter_id == 3: # "View 03: Defines method that returns average number of fav tweets"
        count = db.get_averageFavourite()[0]
        return render_template("average_fav_tweets.html", fav_count=count[0])
    elif filter_id == 4: # "View 04: Defines method that returns a full join of tables"
        join = db.get_locationOfTweet()
        return render_template("full_join_tables.html", join_table=join)
    elif filter_id == 5: # "View 05: Defines method that returns users in the table using UNION and stuff .. lol"
        user = db.get_userid()[0]
        return render_template("union_result.html", user=user[0])
    elif filter_id == 6: # "View 06: Defines method that returns the average retweet count"
        count = db.get_averageRetweet()[0]
        return render_template("avg_retweets.html", count=count[0])
    elif filter_id == 7: # "View 07: Defines method that returns the tweets with china in it"
        tweets = db.get_chinaTweet()
        return render_template("china_tweets.html", message=tweets)
    elif filter_id == 8: # "View 08: Defines method that returns the highest number of tweets in a day"
        count = db.get_maxTweetInDay()[0]
        return render_template("highest_tweet_count.html", count=count[0])
    elif filter_id == 9: # "View 09: Defines method that returns latest tweet view"
        tweet = db.get_latestTweet()[0]
        return render_template("latest_tweet.html", text_id=tweet[0], user_id=tweet[1], msg=tweet[2], date=tweet[3], source=tweet[4], loc=tweet[5])
    elif filter_id == 10: # "View 10: Defines method that returns total number of tweets in the database"
        count = db.get_totalTweets()[0]
        return render_template("count_tweets.html", count=count[0])
    return

# ex http://localhost:5000/api/201960
# TODO add query parameters like http://localhost:5000/api?id=201960
@app.route('/api/<id>', methods=['GET','POST'])
def api(id):
    text_id = id
    tweets = db.get_tweets(text_id)
    return jsonify(tweets)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
