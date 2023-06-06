from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, login_required, logout_user, current_user
import random
from .models import determine_level
from .database import db

bp = Blueprint('views', __name__)

# Login page
@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = User(email)
        login_user(user)
        return redirect('/dashboard')
    else:
        return render_template('login.html')

# Dashboard page
@bp.route('/dashboard')
@login_required
def dashboard():
    # Get the child's latest programming level from MongoDB
    child_data = db.child_data.find_one({'email': current_user.email}, sort=[('timestamp', -1)])
    level = child_data['level']

    # Generate a random project suggestion based on the child's level
    projects = {
        'beginner': [
            'Build a simple calculator',
            'Create a guessing game',
            'Design a basic web page'
        ],
        'intermediate': [
            'Develop a text-based adventure game',
            'Create a blog with comments',
            'Design a responsive web page'
        ],
        'advanced': [
            'Build a full-stack web application',
            'Develop a machine learning model',
            'Design a mobile app'
        ]
    }
    suggestion = random.choice(projects[level])

    return render_template('dashboard.html', level=level, suggestion=suggestion)

# Logout page
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

# Determine level API endpoint
@bp.route('/api/determine_level', methods=['POST'])
def api_determine_level():
    data = request.get_json()
    age = data['age']
    experience = data['experience']
    familiarity = data['familiarity']
    languages = data['languages']
    tools = data['tools']
    complexity = data['complexity']
    level = determine_level(age, experience, familiarity, languages, tools, complexity)

    # Store data in MongoDB
    child_data = {
        'email': current_user.email,
        'age': age,
        'experience': experience,
        'familiarity': familiarity,
        'languages': languages,
        'tools': tools,
        'complexity': complexity,
        'level': level,
        'timestamp': datetime.datetime.utcnow()
    }
    db.child_data.insert_one(child_data)

    response = {
        'level': level
    }
    return jsonify(response)
