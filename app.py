import os
if os.path.exists("env.py"):
  import env
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/stations')
def get_station():
    return render_template("index.html", genre=list(mongo.db.genre.find()))

@app.route('/contact-us')
def contact_us():
    return render_template("contact_us.html",)

@app.route('/genre/<radio_genre>')
def get_radio_details(radio_genre):
    title = ''
    if radio_genre == 'news':
        title = 'News'
    elif radio_genre == 'pop':
        title = 'Pop'
    elif radio_genre == 'classic-hits':
        title = 'Classic Hits'
    elif radio_genre == '80s':
        title = '80s'
    station = mongo.db.station.find({"radio_genre": radio_genre})
    print(station)
    return render_template('station_details.html', station=mongo.db.station.find({"radio_genre": radio_genre}), title=title)

@app.route('/stations/add_station')
def add_station():
    return render_template("add_station.html",  genre=mongo.db.genre.find())


@app.route('/insert_station', methods=['POST'])
def insert_station():
    station = mongo.db.station
    station.insert_one(request.form.to_dict())
    return redirect(url_for('get_station'))


@app.route('/edit_station/<station_id>')
def edit_station(station_id):
    the_station = mongo.db.station.find_one({"_id": ObjectId(station_id)})
    all_genres = mongo.db.genre.find()
    return render_template('edit_station.html', station=the_station,
                           genres=all_genres)


@app.route('/update_station/<station_id>', methods=["POST"])
def update_station(station_id):
    station = mongo.db.station
    station.update({'_id': ObjectId(station_id)}, {
        'radio_genre': request.form.get('radio_genre').lower(),
        'radio_name': request.form.get('radio_name'),
        'radio_website': request.form.get('radio_website'),
        'radio_phone': request.form.get('radio_phone'),
        'radio_description': request.form.get('radio_description'),
        'radio_stream': request.form.get('radio_stream')
    })
    return redirect(url_for('get_station'))


@app.route('/delete_station/<station_id>')
def delete_station(station_id):
    mongo.db.station.remove({'_id': ObjectId(station_id)})
    return redirect(url_for('get_station'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)
