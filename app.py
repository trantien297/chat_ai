from flask import Flask, render_template, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("message")
    with model.chat_session() as session:
        ai_response = session.generate(user_input, max_tokens=200)
    return jsonify({"response": ai_response.strip()})

if __name__ == "__main__":
    app.run(debug=True)
