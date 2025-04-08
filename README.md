# Password Complexity Checker

A Python application that evaluates password strength based on multiple security criteria. The checker analyzes passwords against common security requirements and provides detailed feedback on their strength.

## Features

- Checks password strength against 6 key criteria:
  - Minimum length (8 characters)
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
  - Not a commonly used password
- Provides a strength rating (Weak, Moderate, Strong, Very Strong)
- Displays detailed analysis with visual indicators (✓/✗)

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
```bash
git clone https://github.com/PaenuthSec/Password-Complexity-Checker.git
cd Password-Complexity-Checker
```

2. (Optional) Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
..\venv\Scripts\activate
# On Unix/MacOS:
source venv/bin/activate
```

## Usage

Run the script:
```bash
python password_checker.py
```

The program will:
1. Prompt you to enter a password
2. Analyze the password against security criteria
3. Display the overall strength rating
4. Show a detailed analysis of which criteria were met

Example output:
```
Password Complexity Checker

Enter password to analyze: MyP@ssw0rd

Strength: Very Strong

Detailed Analysis:
- Length ≥8 characters: ✓
- Contains uppercase: ✓
- Contains lowercase: ✓
- Contains numbers: ✓
- Contains special chars: ✓
```

## Password Criteria

For a "Very Strong" password rating, all of the following criteria must be met:
- At least 8 characters in length
- Contains at least one uppercase letter (A-Z)
- Contains at least one lowercase letter (a-z)
- Contains at least one number (0-9)
- Contains at least one special character (!@#$%^&*(),.?":{}|<>)
- Must not be a commonly used password

### Common Password Protection

The checker includes protection against commonly used passwords. Even if a password meets all the basic complexity requirements, it will be flagged if it matches known common passwords (e.g., 'Password123', 'Admin123', etc.). This helps prevent the use of passwords that are:
- Frequently used and predictable
- Commonly found in password breach databases
- Easy to guess despite meeting complexity requirements

### Note on Limitations

While this checker provides good basic security guidelines, for maximum security you should also consider:
- Using a password manager
- Never reusing passwords across different accounts
- Making passwords longer than the minimum 8 characters
- Using randomly generated passwords when possible

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is open source.