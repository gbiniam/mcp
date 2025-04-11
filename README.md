# MCP Code Review

This repository contains the code for the MCP (Model Context Protocol) project. It includes multiple Python scripts and a project structure to facilitate development and testing.

## Project Structure

```
mcp_host.py
mcp_server_a.py
mcp_server_api.py
mcp_server_b.py
logs/
    error.log
project/
    sample_code.py
```

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or later
- pip (Python package manager)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gbiniam/mcp.git
   cd mcp
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate   # On Windows
   ```

3. **Install Required Libraries**:
   Install all necessary Python libraries, including Flask, Requests, and Llama:
   ```bash
   pip install flask requests llama-index
   ```

4. **Run the Application**:
   You can run any of the Python scripts as needed. For example:
   ```bash
   python3 mcp_server_api.py
   ```

## Logs

Logs are stored in the `logs/` directory. Check `error.log` for error details.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.