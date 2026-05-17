README.md
# Password Strength Analyzer

## Overview
The Password Strength Analyzer is a Python-based application designed to evaluate the strength of user-entered passwords. The system checks password length, complexity, uniqueness, and reuse prevention to determine whether a password is Weak, Moderate, Strong, or Very Strong.

This project helps users create secure passwords and improve cybersecurity awareness.

---

# Features

- Check password length
- Analyze password complexity
- Detect uppercase and lowercase characters
- Detect numbers and special characters
- Identify common weak passwords
- Prevent password reuse using hashed passwords
- Display password strength level
- Provide suggestions for stronger passwords
- User-friendly GUI built using Tkinter

---

# Technologies Used

- Python
- Tkinter (GUI)
- Regular Expressions (re)
- Hashlib (SHA-256 hashing)

---

# Project Structure

```bash
Password-Strength-Analyzer/
│
├── password_strength_analyzer.py
├── README.md
```

How It Works

The analyzer checks the following conditions:

Feature	Description
Length Check	Minimum secure length verification
Uppercase Letters	Detect A-Z characters
Lowercase Letters	Detect a-z characters
Numbers	Detect numeric values
Special Characters	Detect symbols like @, #, $, %
Common Password Detection	Rejects weak common passwords
Password Reuse Prevention	Prevents reuse using hashing
Password Strength Levels
Score	Strength
0 - 3	Weak
4 - 6	Moderate
7 - 9	Strong
10+	Very Strong

Example
Input
Password: Hello@123
Output
Password Strength: STRONG

Suggestions:
- Excellent Password! No improvements needed.
GUI Preview Features
Password input field
Analyze Password button
Password strength indicator
Suggestions section
Key Features display
Security Features
Password Hashing

The application uses SHA-256 hashing to securely store previously used passwords.

Password Reuse Prevention

Previously used passwords are detected and rejected for improved security.

Advantages
Easy to use
Beginner-friendly project
Enhances cybersecurity awareness
Helps users create secure passwords
Useful for authentication systems

Author

Developed by: Hansraj Jat

License

This project is open-source and available under the MIT License.
