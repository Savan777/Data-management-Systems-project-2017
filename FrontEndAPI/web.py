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
        print session['user_id'] #user selected input value can be used for compare
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
    if form.validate_on_submit():
        session['filter_id'] = form.name.data
        print session['filter_id']
        return redirect('/table')

    return render_template("filter.html", form=form)


@app.route('/tables', methods=['POST', 'GET'])
def tables():
    filter_id = session['filter_id']
    stats = db.get_all()[0]

    if filter_id == 1:
        #get view 1
        #stats = db.get_stats(player_id)[0]
        return render_template("tables.html", name=stats[1], blocks=stats[9], stl=stats[8], drfgm=stats[11], drfga=stats[12], drfgpct=stats[13])

    elif filter_id == 2:
        #get view 2
        # stats = db.get_stats(player_id)[0]
        return
    elif filter_id == 3:
        # get view 3
        # stats = db.get_stats(player_id)[0]
        return
    elif filter_id == 4:
        # get view 4
        # stats = db.get_stats(player_id)[0]
        return
    elif filter_id == 5:
        # get view 5
        # stats = db.get_stats(player_id)[0]
        return
    elif filter_id == 6:
        # get view 6
        # stats = db.get_stats(player_id)[0]
        return
    elif filter_id == 7:
        # get view 7
        # stats = db.get_stats(player_id)[0]
        return
    elif filter_id == 8:
        # get view 8
        # stats = db.get_stats(player_id)[0]
        return
    elif filter_id == 9:
        # get view 9
        # stats = db.get_stats(player_id)[0]
        return
    elif filter_id == 10:
        # get view 10
        # stats = db.get_stats(player_id)[0]
        return


# create simple api that takes in id and response with stats of said player
# ex http://localhost:5000/api/201960
# TODO add query parameters like http://localhost:5000/api?id=201960
@app.route('/api/<id>', methods=['GET','POST'])
def api(id):
    text_id = id
    tweets = db.get_tweets(text_id)
    return jsonify(tweets)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
