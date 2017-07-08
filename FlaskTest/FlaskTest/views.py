"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect,request,session,url_for,g, jsonify
from FlaskTest import application,db,models,getchartdata
from .forms import LoginForm,ConstraintForm

from flask_login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user ,current_user 

login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = "login"

@application.before_request
def before_request():
    g.user = current_user

@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))


@application.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        remember_me = False
        if 'remember_me' in request.form:
            remember_me = True
        registered_user = models.User.query.filter_by(username=username,password=password).first()
        if registered_user is None:
            flash('Username or Password is invalid' , 'error')
            return redirect(url_for('login'))
        login_user(registered_user, remember = remember_me)
        flash('Logged in successfully')
        return redirect('/home')
   return render_template('login.html', 
                           title='Sign In',
                           form=form)

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@application.route('/usmodeldata/api/', methods=['GET', 'POST'])
def get_usmodeldata():
    if request.method == 'GET':
        test = 1
        return 5
    elif request.method == 'POST':
        content = request.get_json()
        json_channel = content['sport']['channel']
        json_location = content['sport']['timeslot']['location']
        json_datetime = content['sport']['timeslot']['datetime']
        json_team = content['sport']['timeslot']['team']
        json_gamecount = content['sport']['statistics']['gamecount']
        json_homeaway = content['sport']['statistics']['homeaway']
        json_accuracy = content['sport']['statistics']['accuracy']
        if json_channel is None \
            or json_location is None \
            or json_datetime is None \
            or json_team is None \
            or json_gamecount is None \
            or json_homeaway is None \
            or json_accuracy is None:
            return jsonify({"message": "Error."}), 400  
        new_sport = models.Sport(channel=json_channel)
        db.session.add(new_sport)
        db.session.flush()   
        new_timeslot = models.Timeslot(location=json_location,
                                datetime=json_datetime,
                                team = json_team,
                                sport_id =new_sport.id)
        db.session.add(new_timeslot)
        new_statistics = models.Statistics(gamcount=json_gamecount,
                                accuracy=json_accuracy,
                                homeaway=json_homeaway,
                                sport_id=new_sport.id)
        db.session.add(new_statistics)
        db.session.commit()
        return jsonify({'message' :'Attribute Created successfully'}), 200
    return jsonify({"message": "Error."}), 400  

@application.route('/')
@application.route('/home')
@login_required
def home():

    #join us model tables together
    usmodeldata = db.session.query(models.Sport,models.Timeslot,models.Statistics).filter(models.Sport.id == models.Timeslot.sport_id) \
                                 .filter(models.Sport.id == models.Statistics.sport_id).all()
    #Update date to readable format
    for sportdata in usmodeldata:
        sportdata.Timeslot.datetime = datetime.strptime(sportdata.Timeslot.datetime, '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%A %B %Y")

    """Renders the home page."""
    return render_template('index.html',
        title='Home Page',
        film='Bond',
        year=datetime.now().year,
        usmodeldata=usmodeldata,
        base_url = request.url_root)

@application.route('/DeleteSportsData')
@login_required
def DeleteSportsData():
    #join us model tables together
    usmodeldata = db.session.query(models.Sport,models.Timeslot,models.Statistics).filter(models.Sport.id == models.Timeslot.sport_id) \
                                 .filter(models.Sport.id == models.Statistics.sport_id).all()
    for sportdata in usmodeldata:
        db.session.delete(sportdata.Sport)
        db.session.delete(sportdata.Timeslot)
        db.session.delete(sportdata.Statistics)

    db.session.commit()

    
    """Renders the home page."""
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,
        usmodeldata=None,
        base_url = request.url_root)

@application.route('/constraints', methods=['GET', 'POST'])
@login_required
def constraint():
    form = ConstraintForm()
    constraint_current =  db.session.query(models.Constraints).order_by(models.Constraints.id.desc()).first()
    if form.validate_on_submit():
        print(request.form['Constraint5_SelMult'] )
        constraint_formdata = models.Constraints(constraint1_flt = request.form['Constraint1_Flt'] \
                                        ,constraint2_bool =request.form['Constraint2_Bool'] \
                                        ,constraint3_str = request.form['Constraint3_Str'] \
                                        ,constraint4_sel = request.form['Constraint4_Sel'] \
                                        ,constraint5_selmult = request.form['Constraint5_SelMult'] \
                                        ,constraint6_txtarea = request.form['Constraint6_TxtArea'] \
                                        ,constraint7_decimal = request.form['Constraint7_Decimal'])
        db.session.add(constraint_formdata)
        db.session.commit()
        flash('Constraints are updated')
        return render_template('constraints.html',
                form=form,
                constraint_current=constraint_formdata)

    """Renders the constraint page."""
    return render_template('constraints.html',
        form=form,
        constraint_current=constraint_current)



@application.route('/ConstraintJSONGet', methods=['GET'])
def ConstraintJSONGet():

    constraint_current =  models.Constraints.query.order_by(models.Constraints.id.desc()).first()
    if constraint_current is None:
        return jsonify({'message' :'No constraints have been entered'}), 200
    """Use for single row in db."""
    return jsonify(constraint_data=constraint_current.serialize), 200
    """Use for multiple rows in db."""
    #return jsonify(json_list=[i.serialize for i in constraint_current]), 200



@application.route('/charting')
@login_required
def charting():
    """Renders the charting page."""
    return render_template('charting.html',
        title='Sample chart json',
        year=datetime.now().year,
        message='Your application description page.')

@application.route('/accuracybarchart', methods=['POST'])
@login_required
def accuracyBarChart():
    if request.method=='POST':
        filtertype_Accuracy=request.form['filtertype_Accuracy']
        accuracy_data =getchartdata.AccuracyBarChart.accuracydata(filtertype_Accuracy)
        return jsonify(accuracy_data)

    """Sends json data to the charting page."""
    return jsonify({'message' :'No POST found.'}), 200
  
    

