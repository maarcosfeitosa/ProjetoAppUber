from app.templates import app

@app.route("/")
def index():
    return "Hello World"

