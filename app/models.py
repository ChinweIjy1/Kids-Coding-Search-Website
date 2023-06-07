def determine_level(age, experience, familiarity, languages, tools, complexity):
    level = 'Beginner'

    # Check age
    if age >= 12 and age <= 17:
        level = 'Intermediate'
    elif age >= 18:
        level = 'Advanced'

    # Check completed projects
    if completed_projects >= 5:
        level = 'Intermediate'
    elif completed_projects >= 10:
        level = 'Advanced'

    # Check completed courses
    if completed_courses >= 3:
        level = 'Intermediate'
    elif completed_courses >= 6:
        level = 'Advanced'

    # Check languages and tools
    if 'Python' in languages and 'JavaScript' in languages:
        level = 'Intermediate'
    elif 'Python' in languages and 'JavaScript' in languages and 'Git' in tools:
        level = 'Advanced'

    # Check complexity
    if complexity >= 3:
        level = 'Intermediate'
    elif complexity >= 5:
        level = 'Advanced'

    return level

class User:
    def __init__(self, email):
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
	return True
