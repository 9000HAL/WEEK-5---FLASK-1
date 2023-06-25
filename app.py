from flask import Flask, request, render_template



app = Flask(__name__)



#--------ROUTES---------------------

@app.route("/")
def hello_world():
    return "<p>Hello, THIEVES!</p>"



@app.route('/home')
def home():
    return '<h1>This is the home page</h1>'



@app.route('/user/<username>')
def username(username):
    # show the user profile for that user
    return f'Hello {username}!'



@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'




#HTTP methods:

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return '<h1>>Logged In</h1>'
    return render_template('forms.html')



#########STUDENTS EXAMPLE

@app.route('/students')
def students():
    students_lst = ['Gabe', 'Will', 'Sean', 'Peace']
    return render_template('students.html', students_lst=students_lst)


