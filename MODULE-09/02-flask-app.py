from flask import Flask, render_template
app = Flask(__name__)

@app.route("/tiwaribro")
def hi():
    return "hello world"

# # @app.route("/tiwaribro")
# # def greetingbkhbs():
# #     return "hello tiwaribro"


# @app.route("/flask")
# def chingchong():
#     return "<h1 style=\"color:red\">Welcome to China</h1>"

# @app.route('/tiwaribro')
# def tiwaribro():
#     return render_template("index.html")    

# @app.route("/<name>")
# def greetings(name):
#     return "Hello! " + name.upper()

if __name__ == "__main__":
    app.run(debug=True, port=8080)
