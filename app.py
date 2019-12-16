from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return "Hello world"

@app.route("/test/<int:search_query>")
def search(search_query):
    return f"<h1>{search_query} * 100 = {search_query * 100}</h1>"


if __name__ == "__main__":
    app.run()