from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "🐺 Serveur HTTP Les Loups est prêt !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
