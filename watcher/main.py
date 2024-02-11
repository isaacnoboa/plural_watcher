from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_view():
    return render_template('index.html')

@app.route("/webhooks/<webhook_id>/<webhook_token>")
def webhooks_view():
    return render_template('webhooks.html')