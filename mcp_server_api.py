from flask import Flask, request, jsonify
from mcp_server_a import get_code_snippet
from mcp_server_b import get_latest_error
import requests

app = Flask(__name__)

@app.route('/get_code', methods=['GET'])
def get_code():
    return jsonify({"code": get_code_snippet()})

@app.route('/get_log', methods=['GET'])
def get_log():
    return jsonify({"log": get_latest_error()})

@app.route('/review_code', methods=['POST'])
def review_code():
    code = request.json.get("code", "")
    log = request.json.get("log", "")

    prompt = f"""
You are an expert software engineer reviewing code.

Here is the code:
{code}

And here is the error log:
{log}

Please:
1. Analyze the code and determine the issue.
2. Suggest a corrected version if needed.
3. Explain the reason for your fix.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",        # or "mistral" or any model you pulled with Ollama
                "prompt": prompt,
                "stream": False
            }
        )
        result_text = response.json().get("response", "[No response received from model]")
        return jsonify({"result": result_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)
