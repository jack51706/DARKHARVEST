from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db

# Inherit forms from forms.py
from app.forms import LoginForm, RegistrationForm, ShellForm

# Inherit user definitions
from flask_login import current_user, login_user, login_required, logout_user

# Inherit defined user table
from app.models import User

# Inherit url parsing and redirection
from werkzeug.urls import url_parse

# Define routes views

# Home page currently loaded with filler data
@app.route('/')
@app.route('/index')

# Hides behind basic authentication
@login_required
def index():

    shells = [
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        }
    ]


    return render_template('index.html', title='Home', shells=shells)

# Route for connections received.
@app.route('/connections', methods=['GET', 'POST'])

# Hides behind basic authentication
@login_required
def connections():
    form = ShellForm()
    shells = [
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        },
        {
            'id': '1',
            'ip': '176.22.45.98',
            'os': 'Windows 7 Pro', 
            'priv': 'SYSTEM',
            'compuser': 'ClientDC/DCAdmin',
            'heartbeat': ' 14 minutes ago'
        }
    ]


    return render_template('connections.html', title='Connections', shells=shells, form=form)


# Route for geo-locating connections received.
@app.route('/map')

# Hides behind basic authentication
@login_required
def map():
    return render_template('map.html', title='Map')


# Route for aggregating and parsing loot.
@app.route('/loot')

# Hides behind basic authentication
@login_required
def loot():
    return render_template('loot.html', title='Loot')

# Route for geo-locating connections received.
@app.route('/help')

def help():
    return render_template('help.html', title='Help')

# Route for main application login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# Route for UI logout 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Route for UI account registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



# ------------------------------------------
# API
# ------------------------------------------
    
# Return info on a specific shell
@app.route('/api/shells/<id>', methods=['GET'])                                                                                                    
def shell_info():                                                                                                                              
    data = request.get_json()
    # ... do your business logic, and return some response
    # e.g. below we're just echo-ing back the received JSON data
    return jsonify(data)

def run_command():
    pass

# Return info on all current shells
@app.route('/api/shells', methods=['GET'])                                                                                                    
def all_shells():                                                                                                                              
    data = request.get_json()
    # ... do your business logic, and return some response
    # e.g. below we're just echo-ing back the received JSON data
    return jsonify(data)

@app.route('/api/shells', methods=['POST'])                                                                                                    
def new_shell():                                                                                                                              
    data = request.get_json()
    # ... do your business logic, and return some response
    # e.g. below we're just echo-ing back the received JSON data
    return jsonify(data)

@app.route('/api/shells/<id>', methods=['DELETE'])                                                                                                    
def delete_shell():                                                                                                                              
    data = request.get_json()
    # ... do your business logic, and return some response
    # e.g. below we're just echo-ing back the received JSON data
    return jsonify(data)