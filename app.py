from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>⚽ MatchEdge AI</h1>
    <p>Proyecto funcionando correctamente.</p>
    <p>Versión 1.0</p>
    """
