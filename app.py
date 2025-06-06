from flask import Flask

# __name__ = __main__  significa que eu to executando o projeto  de forma manual e esta em desenvolvimento
app = Flask(__name__)

@app.route("/")
def hello_Word():
    return "Macaco Programas 🐒 💻 "

@app.route("/about")
def about():
    return "Pagina Sobre"

@app.route("/task")
def task():
    return "pagina teste de salvamento"

if __name__ == "__main__":
    app.run(debug=True)