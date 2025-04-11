def get_code_snippet(filename="project/sample_code.py"):
    with open(filename, "r") as f:
        return f.read()
