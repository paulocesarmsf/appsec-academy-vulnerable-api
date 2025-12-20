# Vulnerable API - AppSec Academy

## ⚠️ WARNING: INTENTIONALLY VULNERABLE

**This repository contains intentionally vulnerable code for educational purposes only.**

This is a deliberately insecure Flask application designed to demonstrate security vulnerabilities, specifically **Command Injection**. **DO NOT** use this code in production environments or expose it to untrusted networks.

## Purpose

This repository is part of an educational initiative to teach application security concepts. It demonstrates common security vulnerabilities in web applications, allowing security researchers, developers, and students to:

- Understand how security vulnerabilities can be introduced in code
- Learn to identify and exploit common vulnerabilities
- Practice secure coding practices by understanding what NOT to do
- Test security scanning tools and techniques

## Technology Stack

- **Python 3**
- **Flask** - Web framework
- **OS Module** - System command execution (vulnerable implementation)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd appsec-academy-vulnerable-api
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask development server:
```bash
python app.py
```

The API will be available at `http://localhost:5001`

## API Endpoints

### GET `/`
Returns API information and available endpoints.

**Example:**
```bash
curl http://localhost:5001/
```

### GET `/list`
Lists the contents of a specified folder. **VULNERABLE TO COMMAND INJECTION**

**Parameters:**
- `folder` (query parameter): Name of the folder to list

**Example (Normal Usage):**
```bash
curl "http://localhost:5001/list?folder=./"
```

**⚠️ VULNERABILITY DEMONSTRATION:**
This endpoint is vulnerable to command injection. The user input is directly concatenated into a system command without sanitization.

**Example Exploits:**
```bash
# Command injection examples (for educational purposes only)
curl "http://localhost:5001/list?folder=./; id"
curl "http://localhost:5001/list?folder=./ && whoami"
curl "http://localhost:5001/list?folder=./ | cat /etc/passwd"
```

## Security Vulnerability

### Command Injection (CWE-78)

**Location:** `/list` endpoint in `app.py`

**Vulnerable Code:**
```python
folder = request.args.get('folder', '.')
result = os.popen(f'ls -la {folder}').read()
```

**Issue:**
The application directly concatenates user input (`folder` parameter) into a system command without any validation or sanitization. This allows attackers to inject arbitrary commands that will be executed on the server.

**Why This is Dangerous:**
- Arbitrary command execution on the server
- Potential for data exfiltration
- System compromise
- Unauthorized access to sensitive files

**Secure Alternatives:**
- Use `os.listdir()` or `pathlib` instead of shell commands
- Validate and sanitize all user inputs
- Use allowlists for acceptable values
- Never concatenate user input into system commands

## Educational Use Only

This repository is intended for:
- Security education and training
- Learning secure coding practices
- Understanding common vulnerabilities
- Testing security tools in a controlled environment

**DO NOT:**
- Deploy to production
- Expose to public networks
- Use as a reference for secure code
- Include in production codebases

## Disclaimer

This software is provided for educational purposes only. The authors and contributors are not responsible for any misuse or damage caused by this code. Use at your own risk and only in isolated, controlled environments.

## Contributing

Contributions that add more intentional vulnerabilities (with proper documentation) for educational purposes are welcome. Please ensure all vulnerabilities are clearly documented and marked as intentional.

## License

[Specify your license here]

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE-78: OS Command Injection](https://cwe.mitre.org/data/definitions/78.html)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/latest/security/)

