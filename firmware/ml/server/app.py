# NeoGuard - Flask Dashboard Server
# Handles data storage, clinical reports, and UI.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "NeoGuard Clinical Dashboard - Coming Soon"

if __name__ == '__main__':
    app.run(debug=True)
