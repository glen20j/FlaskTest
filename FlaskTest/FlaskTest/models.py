from FlaskTest import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(20), unique=True , index=True)
    password = db.Column(db.String(10))
    email = db.Column(db.String(50),unique=True , index=True)
    registered_on = db.Column(db.DateTime)
 
    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)

#Handle the US schedule data sent to our server
class Sport(db.Model):
    __tablename__ = 'usmodeldata_sport'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    channel  = db.Column(db.String(80))# does site have a formal name
    datetime_received =db.Column(db.DateTime)
    timeslot = db.relationship("Timeslot", backref='sport', lazy='dynamic')
    statistics = db.relationship("Statistics", backref='sport', lazy='dynamic')

    def __init__(self , channel):
        self.channel = channel
        self.datetime_received = datetime.utcnow()

    def __repr__(self):
        return '< %r>' % (self.channel)

class Timeslot(db.Model):
    __tablename__ = 'usmodeldata_timeslot'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(80))
    datetime = db.Column(db.String(80))
    team = db.Column(db.String(80))
    sport_id = db.Column(db.Integer, db.ForeignKey('usmodeldata_sport.id'))

    def __init__(self , location,datetime,team,sport_id):
        self.location = location
        self.datetime = datetime
        self.team = team
        self.sport_id=sport_id

    def __repr__(self):
        return '< %r>' % (self.team)


class Statistics(db.Model):
    __tablename__ = 'usmodeldata_statistics'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gamcount = db.Column(db.Float(20))
    homeaway = db.Column(db.String(80))
    accuracy = db.Column(db.Float(20))
    sport_id = db.Column(db.Integer, db.ForeignKey('usmodeldata_sport.id'))

    def __init__(self , gamcount,homeaway,accuracy,sport_id):
        self.gamcount = gamcount
        self.homeaway = homeaway
        self.accuracy = accuracy
        self.sport_id = sport_id

    def __repr__(self):
        return '< %r>' % (self.gamcount)



class Constraints(db.Model):
    __tablename__ = 'constraints'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    constraint1_flt = db.Column(db.Float(20))
    constraint2_bool = db.Column(db.Boolean)
    constraint3_str = db.Column(db.String(80))
    constraint4_sel = db.Column(db.String(80))
    constraint5_selmult = db.Column(db.String(80))
    constraint6_txtarea = db.Column(db.String(200))
    constraint7_decimal = db.Column(db.Float)
    createddate = db.Column(db.DateTime)

    def __init__(self , constraint1_flt ,constraint2_bool , constraint3_str,constraint4_sel,constraint5_selmult,constraint6_txtarea,constraint7_decimal):
        self.constraint1_flt = constraint1_flt
        self.constraint2_bool = constraint2_bool
        self.constraint3_str = constraint3_str
        self.constraint4_sel = constraint4_sel
        self.constraint5_selmult = constraint5_selmult
        self.constraint6_txtarea = constraint6_txtarea
        self.constraint7_decimal = constraint7_decimal
        self.createddate = datetime.utcnow()
        pass

    def __repr__(self):
        return '< %r>' % (self.createddate)

    #used to return dictionary items for easy jsonify  (datetime value can cause jsonify issues)
    @property
    def serialize(self):
        return {
            'constraint1_flt': self.constraint1_flt, 
            'constraint2_bool': self.constraint2_bool,
            'constraint3_str': self.constraint3_str,
            'constraint4_sel': self.constraint4_sel,
            'constraint5_selmult': self.constraint5_selmult,
            'constraint6_txtarea': self.constraint6_txtarea,
            'constraint7_decimal': self.constraint7_decimal,
            'createddate': [self.createddate.strftime("%Y-%m-%d"), self.createddate.strftime("%H:%M:%S")]
        }






















#class USModelData(db.Model):
#    __tablename__ = 'usmodeldata'
#    id = db.Column(db.Integer , primary_key=True)
#    date_received = db.Column(db.DateTime)

#    varone =  db.Column(db.String(120),index=True)
#    vartwo =  db.Column(db.String(120),index=True)

#    def __init__(self , model_data):
#        self.model_data = model_data
#        self.date_received = datetime.utcnow()

#    def __repr__(self):
#        return '<Model Data %r>' % (self.model_data)




#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    nickname = db.Column(db.String(64), index=True, unique=True)
#    email = db.Column(db.String(120), index=True, unique=True)
#    posts = db.relationship('Post', backref='author', lazy='dynamic')

#    def __repr__(self):
#        return '<User %r>' % (self.nickname)

#class Post(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    body = db.Column(db.String(140))
#    timestamp = db.Column(db.DateTime)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#    def __repr__(self):
#        return '<Post %r>' % (self.body)