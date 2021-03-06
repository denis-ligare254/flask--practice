from flask import  Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('welcome.html')



# 1.jinja2 templete
# 2.werkzeug http and routing
# 3.development server and debugger

# to  run the project
# 1.export FLASK_APP="NAMEOFPROJECT" it tells flask which module our application can be found
# 2.export FLASK_ENV=development-To switch Flask to the development environment and enable debug mode.it enables some design features like the debugger
# select interpreter(to solve "cannot import module flask") by clicking cntrl shift p