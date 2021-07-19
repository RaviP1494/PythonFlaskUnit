from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from random import randint

app = Flask(__name__)

app.config['SECRET_KEY'] = "thisisthekey"
#app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def home():
    """Home page in root route demo"""
    html = """
            <html>
                <body>
                    <h1>Home Page</h1>
                    <a href='/hello'>Hi page</a>
                    <br>
                    <a href='/addcomment'>Comment!</a>
                </body>
            </html>
            """
    return html


@app.route('/hello')
def say_hello():
    """Return simple 'hello' greeting in flask basics demo"""
    html = """
            <html>
                <body>
                    <h1>Hello</h1>
                </body>
            </html>
            """
    return html


@app.route('/querystringtest')
def query_string_test():
    """Parses query string into more legible format in query string demo"""
    response = ''
    for item in request.args:
        response+= f"<h4>{item}:{request.args[item]}</h4>"
    
    return response
    

@app.route('/postrequestpage',methods=["POST"])
def post_request_page():
    """Makes a post request in POST request demo"""

    return 'this was a POST request'


@app.route('/addcomment')
def add_comment_form():
    """Serves a comment form to be POSTed in form submission demo"""

    html = """
            <html>
                <body>
                    <form method='POST'>
                        <input name= 'comment' type='text' placeholder='comment' required>
                        <button>Submit</button>
                    </form>
                </body>
            </html>
            """
    return html


@app.route('/addcomment',methods=["POST"])
def post_comment():
    """Posts comment to page in form submission demo"""

    comment = request.form["comment"]
    return f"You commented: \n {comment}"


@app.route('/comments/<int:id>')
def show_comment(id):
    """Shows comment number <id> in path variable demo"""
    #int in route path is optional, specifies that path variable is int

    html = f"""
        <html>
            <body>
                <p>You've reached comment number {id}</p>
            </body>
        </html>
    """
    return html


#let's pretend there's a function here to showcase the incredible difficulty of using multiple path variables in one route path


@app.route('/templates/hello')
def jinja_hello():
    """Demo of Jinja to render static template of hello.html"""

    return render_template('hello.html')


@app.route('/lucky')
def lucky_page():
    """Demo of dynamic HTML template using Jinja by making a page that displays a random lucky number"""

    lucky_num = randint(1,20)
    #inside lucky.html, the variable is named lucky_var and we can use it inside {{ }}
    return render_template('lucky.html',lucky_num = lucky_num)


@app.route('/base')
def base_temp():
    """Demo of template inheritance, base template"""

    return render_template('base.html')


@app.route('/child')
def child_temp():
    """Demo of template inheritance, child template"""

    return render_template('child.html')


@app.route('/funform')
def funform_view():
    """Returns simple name submission form"""

    return render_template('funform.html')


name = 'ravi'
@app.route('/funform', methods=["POST"])
def funform_post():
    """Saves name to global variable"""
    name = request.form.get("name",default="kiran")
    return redirect('/funformdone')


@app.route('/funformdone')
def funformdone_view():
    return name