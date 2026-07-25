# Password Strength Checker

A Python application that evaluates the strength of user passwords based on security best practices. The program checks password policy compliance, calculates password entropy, detects common dictionary passwords, classifies password strength, and provides actionable suggestions to improve security.

## Features

- Checks password length
- Verifies uppercase and lowercase letters
- Detects digits and special characters
- Calculates password entropy
- Detects common passwords using a dictionary file
- Classifies passwords as:
  - Weak
  - Moderate
  - Strong
  - Exceptional
- Provides recommendations to create stronger passwords

## Technologies Used

- Python 3
- math module
- string module

## Project Structure

```
Password-Strength-Checker/
│── password_checker.py
│── common_passwords.txt
└── README.md
```

## How to Run

1. Clone the repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python password_checker.py
```

4. Enter a password when prompted to receive a security analysis.

## Sample Output

```
Enter your password: Abc@1234

Length: 8
Uppercase: True
Lowercase: True
Digits: True
Special: True
Entropy: 52.44 bits
Dictionary Check: Not Found
Strength: Strong

Suggestions:
- Use at least 12 characters.
```

## Author

Rishabh Singh Tomar
