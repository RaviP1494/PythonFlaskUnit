from stories import story
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = 'ravi'




@app.route('/')
def home_view():
    prompts = story.prompts
    return render_template('form.html',prompts=prompts)


@app.route('/story')
def story_view():
    final_story = story.generate(request.args)
    return render_template('story.html',story=final_story)