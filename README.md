# AI PERSONAL ASSISTANT [MINOR PROJECT]

A simple website where you can **ask any question** and **summarize long emails** in seconds, using AI.

This is a **minor project** built with Python (Flask) and the Groq AI service. It is designed to be easy to run, even if you are new to programming.

---

## What Can It Do?

| Tool | What you do | What you get |
|---|---|---|
| **Ask Anything** | Type any question | A clear answer from the AI |
| **Summarize Email** | Paste a long email | A short 2-3 sentence summary |

---

## Before You Start

You will need:

1. **Python 3.9 or newer.** Download it from [python.org](https://www.python.org/downloads/). To check if you already have it, run `python --version` in a terminal.
2. **A free Groq API key.** This is like a password that lets the app use the AI.
   - Go to [console.groq.com/keys](https://console.groq.com/keys)
   - Sign up and click **Create API Key**
   - Copy the key (it starts with `gsk_`)

---

## How to Run It (Step by Step)

**Step 1. Download the project**

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

No Git? Click the green **Code** button on GitHub, choose **Download ZIP**, then unzip it.

**Step 2. Install the required tools**

```bash
pip install flask python-dotenv openai
```

**Step 3. Add your API key**

Create a file named `.env` in the project folder (next to `app.py`) and put this inside, using your own key:

```
GROQ_API_KEY=gsk_your_key_here
```

Do not add quotes or spaces around the `=`.

**Step 4. Start the app**

```bash
python app.py
```

**Step 5. Open it in your browser**

Go to **http://127.0.0.1:5000**. You should see the app. To stop it, press `Ctrl + C` in the terminal.

---

## Something Not Working?

| What you see | What it means | How to fix it |
|---|---|---|
| `GROQ_API_KEY not found` | The app cannot find your key | Check that the `.env` file is in the same folder as `app.py` |
| `401` or "invalid API key" | The key is wrong | Copy it again from the Groq console. It must start with `gsk_` |
| `404 model not found` | Groq removed or renamed the AI model | Add a line like `GROQ_MODEL=openai/gpt-oss-120b` to `.env` |
| `429` error | Too many requests too quickly | Wait a minute and try again |
| Changed `.env` but nothing happened | The app reads `.env` only at startup | Stop the app and run it again |
| `pip` or `python` not recognized | Python is not set up | Reinstall Python and tick **Add Python to PATH** |

---

## Project Files

```
├── app.py               The main program (backend)
├── templates/
│   └── index.html       The web page
├── static/
│   └── style.css        Colors and design
├── .env                 Your secret key (never share this)
└── README.md            This guide
```

---

## How It Works (Simple Explanation)

1. You type something on the web page.
2. The page sends it to the Flask program (`app.py`).
3. Flask passes it to the Groq AI and waits for a reply.
4. The reply is shown back on the page.

The app automatically picks an available AI model, so it keeps working when Groq changes its model list.

---

## Built With

- **Python and Flask** for the backend
- **Groq API** for the AI (used through the `openai` Python package)
- **HTML, CSS and JavaScript** for the web page

---

## Safety Tips

- **Never upload your `.env` file to GitHub.** Create a file named `.gitignore` and add a line containing `.env`.
- If you accidentally share your key, delete it in the Groq console and create a new one.

---

## Project Details

| | |
|---|---|
| **Project Type** | Minor Project |
| **Submitted by** | Your Name |
| **Course / Branch** | Your Course |
| **Institute** | Your College |
| **Guide** | Guide's Name |

---

## Ideas for the Future

- Remember previous messages in a chat
- Choose how long or short the summary should be
- Put the app online for everyone to use

---

If this project helped you, please give it a star on GitHub.
