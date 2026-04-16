from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/text", methods=["POST"])
def text():

    text = request.form.get("text")

    uzunlik = len(text)

    return f"Matn uzunligi: {uzunlik} ta harf"

app.run(debug=True)
