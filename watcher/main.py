from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_view():
    return render_template('index.html')

@app.route("/webhooks/<webhook_id>/<webhook_token>")
def webhooks_view(webhook_id, webhook_token):
    return render_template('webhooks.html',
                            webhook_id=webhook_id,
                            webhook_token=webhook_token)