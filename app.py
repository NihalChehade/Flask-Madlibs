from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

from stories import story

app = Flask(__name__)

app.config['SECRET_KEY']= "something"
debug = DebugToolbarExtension(app)

@app.route("/")
def submit_form(): 
    """Generate form to ask questions"""
    prompts = story.prompts   
    return render_template("form.html", prompts=prompts)

@app.route("/story")
def get_story():
    """Generate the story msg"""
    story_text = story.generate(request.args)
    return render_template("story.html", msg=story_text)


