from flask import Blueprint, jsonify, request
from .models import determine_level
from .database import db

bp = Blueprint('api', __name__)

# Determine level API endpoint
@bp.route('/determine_level', methods=['POST'])
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
        'email': data['email'],
        'age': age,
        'experience': experience,
        'familiarity': familiarity,
        'languages': languages,
        'tools': tools,
        'complexity': complexity,
        'level': level,
    }
    db.child_data.insert_one(child_data)

    response = {
        'level': level
    }
    return jsonify(response)
