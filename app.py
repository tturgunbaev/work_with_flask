from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
@app.route('/hello')
def hello_world():
    return "Hello world"

@app.route("/test/<int:search_query>")
def search(search_query):
    return f"<h1>{search_query} * 100 = {search_query * 100}</h1>"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "toigonbai":
        return f"<h1>I love you {name}</h1>", 200
    else:
        return f"<h1>I don't love you {name}</h1>", 404


if __name__ == "__main__":
    app.run()