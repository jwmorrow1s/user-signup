from flask import request, Flask, redirect
import jinja2
import os
import re


template_dir = os.path.join(os.path.dirname(__file__),"templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)

@app.route("/")
def index():
    template = jinja_env.get_template("index.html")
    return template.render(username="",
                           password="",
                           v_password="",
                           email="",
                           error_user=False,
                           error_pw=False,
                           error_vpw=False,
                           error_email=False)
@app.route("/signup", methods=["POST"])
def signup():
    template = jinja_env.get_template("index.html")
    username = request.form['username']
    password = str(request.form['password'])
    v_password = request.form['password-verification']
    email = str(request.form['email'])
    error_user = False
    error_pw = False
    error_vpw = False
    error_email = False
    if not username:
        error_user = True
    if (len(password) < 3) or (len(password) > 20) or (len(password) == 0):
        error_pw = True
    if (not v_password) or (v_password != password):
        error_vpw = True
    if (len(email) > 0) and not (re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)):
        error_email = True
    if error_user or error_pw or error_vpw or error_email:
        
        return template.render(username="",
                               password="",
                               v_password="",
                               email="",
                               error_user=error_user,
                               error_pw=error_pw,
                               error_vpw=error_vpw,
                               error_email=error_email)
    else:
        return redirect("/welcome?username=" + username)

@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.args.get("username")
    template = jinja_env.get_template("welcome.html")
    return template.render(user=user)

app.run(debug=True)
