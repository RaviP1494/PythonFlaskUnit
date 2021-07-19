from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ravi'

#debug = DebugToolbarExtension(app)

responses = []

satisurv = surveys.satisfaction_survey

@app.route('/')
def home():
    responses.clear()
    return render_template('home.html', survey = satisurv)

@app.route('/questions/<int:id>')
def question(id):
    if len(responses) != id:
        flash("Stop messing with the URL, ANSWER THE QUESTIONS")
        return redirect('/')
    return render_template('question.html', survey = satisurv, id=id)

@app.route('/questions/<int:id>', methods=['POST'])
def question_post(id):
    choice = request.form.get('ans', default='No answer')
    responses.append(choice)

    if id + 1 < len(satisurv.questions):
        return redirect(f'/questions/{id+1}')
    else:
        return redirect(f'/answers')

@app.route('/answers')
def answers():
    if len(responses) != len(satisurv.questions):
        flash("Stop messing with the URL, ANSWER THE QUESTIONS")
        return redirect('/')
    return render_template('/answers.html', answers = responses, survey = satisurv)