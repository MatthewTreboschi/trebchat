# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
import flask_sqlalchemy
import flask_socketio
import models
import bot

MESSAGES_RECEIVED_CHANNEL = 'messages received'

app = flask.Flask(__name__)
mattbot = bot.mattbot()

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

database_uri = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app


db.create_all()
db.session.commit()

def emit_all_messages(channel):
    all_messages = [ \
        db_message.message for db_message in \
        db.session.query(models.Trebchat).all()
    ]
    
    all_names = [ \
        db_name.names for db_name in \
        db.session.query(models.Trebchat).all()
    ]
    db.session.remove()
    socketio.emit(channel, {
        'allMessages': all_messages,
        'allNames': all_names
    })


@socketio.on('connect')
def on_connect():
    sid=flask.request.sid
    print('Someone connected!')
    db.session.add(models.activeusers(sid, "Anonymous"))
    db.session.commit()
    c = models.activeusers.query.filter_by().count()
    socketio.emit('connected', {
        'connectCount': c
    })
    db.session.remove()
    
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    
@socketio.on('disconnect')
def on_disconnect():
    sid=flask.request.sid
    print ('Someone disconnected!')
    user = db.session.query(models.activeusers).filter(models.activeusers.sid==sid).first()
    db.session.delete(user)
    db.session.commit()
    c = models.activeusers.query.filter_by().count()
    socketio.emit('connected', {
        'connectCount': c
    })
    db.session.remove()
    
    
@socketio.on('new message input')
def on_new_message(data):
    sid=flask.request.sid
    print("Got an event for new message input with data:", str(data["message"]))
    user = db.session.query(models.activeusers).filter(models.activeusers.sid==sid).first()
    db.session.add(models.Trebchat(data["message"], user.username));
    if (str(data["message"])[0:2]=="!!"):
        botsaid = mattbot.message(data["message"])
        db.session.add(models.Trebchat(botsaid, "mattbot"))
    db.session.commit();
    
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    
@socketio.on('new name input')
def on_new_name(data):
    sid = flask.request.sid
    user = db.session.query(models.activeusers).filter(models.activeusers.sid==sid).first()
    user.username = data["name"]
    db.session.commit()
    print(data["name"])
    
@app.route('/')
def index():
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

    return flask.render_template("index.html")

if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
