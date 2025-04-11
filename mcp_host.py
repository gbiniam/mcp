import requests

def get_code_snippet():
    res = requests.get("http://localhost:5001/get_code")
    return res.json().get("code")

def get_latest_error():
    res = requests.get("http://localhost:5001/get_log")
    return res.json().get("log")

def request_review(code, log):
    res = requests.post("http://localhost:5001/review_code", json={
        "code": code,
        "log": log
    })
    return res.json().get("result")

def main():
    print("MCP AI Code Review Assistant")

    code = get_code_snippet()
    print("\nCode Snippet:\n", code)

    log = get_latest_error()
    print("\nLatest Error:\n", log)

    print("\n Requesting Review...\n")
    review = request_review(code, log)
    print("LLAMA Response:\n", review)

if __name__ == "__main__":
    main()
