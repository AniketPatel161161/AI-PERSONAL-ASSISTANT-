from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")


if not api_key:
    raise RuntimeError("GROQ_API_KEY not found. Check your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
    timeout=60,
)
PREFERRED = ["openai/gpt-oss-120b", "openai/gpt-oss-20b", "llama-3.1-8b-instant"]

def pick_model():
    env_model = os.getenv("GROQ_MODEL")
    if env_model:
        return env_model
    available = {m.id for m in client.models.list().data}
    for name in PREFERRED:
        if name in available:
            return name
    raise RuntimeError(f"None of the preferred models are available. Your key has: {sorted(available)}")

MODEL = pick_model()
print("Using model:", MODEL)


def ask_llm(system_prompt, user_prompt, temperature=0.7, max_tokens=1000):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        answer = ask_llm("Act like a helpful personal assistant", question)
        return jsonify({"response": answer}), 200
    except Exception as e:
        print("ERROR in /ask:", e)
        return jsonify({"error": str(e)}), 500


@app.route("/summarize", methods=["POST"])
def summarize():
    email_text = request.form.get("email")
    if not email_text:
        return jsonify({"error": "No email text provided"}), 400

    prompt = f"Summarize the following email in 2-3 sentences: {email_text}"

    try:
        summary = ask_llm(
            "Act like an expert email assistant",
            prompt,
            temperature=0.3,
        )
        return jsonify({"response": summary}), 200
    except Exception as e:
        print("ERROR in /summarize:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)