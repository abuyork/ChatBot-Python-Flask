from flask import Flask, render_template, request, jsonify
import config
import openai
import aiapi

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods =["GET","POST"])
def chat():
    if request.method == 'POST':
        msg =request.form["msg"]
        input = msg
        return aiapi.get_Chat_response(input)

if __name__ == '__main__':
    app.run()    



