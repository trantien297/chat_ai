import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)

# === Khởi tạo model ===
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", allow_download=True)

# Đọc cấu hình bot từ config.json
with open("ai_config.json", "r", encoding="utf-8") as f:
    bot_config = json.load(f)


# === Đường dẫn thư mục lịch sử ===
HISTORY_DIR = "./history"
os.makedirs(HISTORY_DIR, exist_ok=True)

# === Lấy đường dẫn file theo ngày ===
def get_history_path():
    today = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(HISTORY_DIR, f"chat_history_{today}.json")

# === Load / save lịch sử theo ngày ===
def load_history():
    path = get_history_path()
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_history(history):
    path = get_history_path()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("message")
    history = load_history()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Thêm câu hỏi người dùng
    history.append({
        "role": "user",
        "content": user_input,
        "timestamp": timestamp
    })

    bot_intro = f"{bot_config['bot_name']} ({bot_config['description']}) đang hỗ trợ bạn.\n"

    # Ghép lịch sử thành prompt
    chat_history = "\n".join([f"{item['role']}: {item['content']}" for item in history])

    prompt = bot_intro + chat_history + "\nassistant:"

    with model.chat_session():
        ai_response = model.generate(prompt, max_tokens=200).strip()

    # Thêm phản hồi AI
    history.append({
        "role": "assistant",
        "content": ai_response,
        "timestamp": timestamp
    })

    save_history(history)

    return jsonify({"response": ai_response})

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)

