from flask import Flask, request

app = Flask(__name__)


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
    return f"You've reached comment number {id}"


#let's pretend there's a function here to showcase the incredible difficulty of using multiple path variables in one route path