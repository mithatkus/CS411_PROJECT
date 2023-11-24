import flask
from flask import Flask, Response, request, flask_login, render_template, redirect, url_for
import mysql.connector
import math
import os, base64

mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'holy guacamole' #CHANGE THIS TO SOMETHING SECURE

#these are for database credentials
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'outthewazoo'
app.config['MYSQL_DATABASE_DB'] = 'historicolor'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


#THIS IS TEMPLATE CODE FOR REFERENCE ON HOW TO PULL DATA FROM THE DATABASE
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM your_table")
    # result = cursor.fetchall()
#THIS IS TEMPLACE CODE FOR REFERENCE ON HOW TO PULL DATA FROM THE DATABASE

def calc_score(guess_color, acutal_color):
    #not really sure how this will actually look when its fully implemented, but for now im
    #going to assume that the inputs are held as arrays of rbg values eg: [255, 255, 255]
    score = 0
    assert len(guess_color) == len(actual_color)
    for i in range(len(guess_color)):
        score += calc_helper(guess_color[i], actual_color[i])
    return score

def calc_helper(guess, actual):
    max_score = 100
    max_deviation = 30

    deviation = abs(guess - actual)

    # force the deviation to not exceed max_deviation
    deviation = min(deviation, max_deviation)

    # trying out an exponential decay function to calculate the score
    score = max_score * math.exp(-deviation / max_deviation)
    return math.floor(score)
    # for some reason once you make a score thats worse than a certain
    # threshhold it always returns a score of 36, dont wanna fix rn


def display_scores():
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM scores ORDER BY score LIMIT 10")
    return cursor.fetchall()

def save_user_score(name, score):
    assert type(name) == str
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (name, score) VALUES (%s, %s)", (name, score))
    conn.commit()
    return

def get_image():
    return

def find_dominant_color(image):
    return


