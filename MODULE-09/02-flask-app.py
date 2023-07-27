from flask import Flask, render_template
app = Flask(__name__)

# @app.route("/tiwaribro")
# def hi():
#     return "hello world"

@app.route("/tiwaribro")
def greetingbkhbs():
    return "hello tiwaribro"


@app.route("/flask")
def chingchong():
    return "<h1 style=\"color:red\">Welcome to China</h1>"

@app.route('/htmlroute')
def tiwaribro():
    return render_template("index.html")    

# dynamic routing 
@app.route("/<name>")
def greetings(name):
    return "Hello! " + name.capitalize()
# for output http://127.0.0.1:8080/ankush

if __name__ == "__main__":
    app.run(debug=True, port=8080)
