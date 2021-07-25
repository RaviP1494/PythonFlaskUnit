from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ravi'

#debug = DebugToolbarExtension(app) 

satisurv = surveys.satisfaction_survey

@app.route('/')
def home():
    return render_template('home.html', survey = satisurv)

@app.route('/start', methods=['POST'])
def start():
    session['responses']=[]
    return redirect('/questions/0')

@app.route('/questions/<int:id>')
def question(id):
    if len(session['responses']) != id:
        flash("Stop messing with the URL, ANSWER THE QUESTIONS")
        return redirect('/')
    return render_template('question.html', survey = satisurv, id=id)

@app.route('/questions/<int:id>', methods=['POST'])
def question_post(id):
    choice = request.form.get('ans', default='No answer')
    responses = session['responses']
    responses.append(choice)
    session['responses'] = responses

    if id + 1 < len(satisurv.questions):
        return redirect(f'/questions/{id+1}')
    else:
        return redirect('/answers')

@app.route('/answers')
def answers():
    if len(session['responses']) != len(satisurv.questions):
        flash("Stop messing with the URL, ANSWER THE QUESTIONS")
        return redirect('/')
    return render_template('/answers.html', survey = satisurv)