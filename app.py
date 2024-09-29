from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html', css_file='stylelogin.css')

@app.route('/create')
def create_profile():
    return render_template('createProfile.html', css_file='styleCreateProfile.css')

@app.route('/profile')
def profile_card():
    return render_template('profileCard.html', css_file='profileCardStyle.css')

@app.route('/preferences')
def roommate_preferences():
    return render_template('roommatePref.html', css_file='styleRoommatePref.css')

@app.route('/swipes')
def swipes():
    return render_template('swipes.html', css_file='swipesStyle.css')

@app.route('/matches')
def matches():
    return render_template('matches.html', css_file='styleMatches.css')

if __name__ == '__main__':
    app.run(debug=True)
