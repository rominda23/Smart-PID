from flask import Flask, request, jsonify
from pathlib import Path

app = Flask(__name__)
DOCS_DIR = Path(__file__).resolve().parent.parent / "markdown-kb"


@app.route("/getDoc")
def get_doc():
    topic = request.args.get("topic")
    if not topic:
        return jsonify({"error": "Missing topic parameter"}), 400

    file_path = DOCS_DIR / f"{topic}.md"
    if not file_path.exists():
        return jsonify({"error": "Document not found"}), 404

    content = file_path.read_text(encoding="utf-8")
    return jsonify({"title": topic, "content": content})


# 👇 Required by Vercel — expose app as 'handler'
handler = app
