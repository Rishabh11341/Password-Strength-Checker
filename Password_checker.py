import math
import string

password = input("Enter your password: ")

length = len(password)

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in string.punctuation for c in password)

print("Length:", length)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Digits:", has_digit)
print("Special:", has_special)

charset = 0

if has_lower:
    charset += 26

if has_upper:
    charset += 26

if has_digit:
    charset += 10

if has_special:
    charset += 32

if charset > 0:
    entropy = length * math.log2(charset)
else:
    entropy = 0

print(f"Entropy: {entropy:.2f} bits")

with open("common_passwords.txt", "r") as file:
    common_passwords = [line.strip() for line in file]

is_common = password.lower() in common_passwords

print("Dictionary Check:", "Found" if is_common else "Not Found")

if is_common:
    strength = "Weak"
elif entropy < 28:
    strength = "Weak"
elif entropy < 36:
    strength = "Moderate"
elif entropy < 60:
    strength = "Strong"
else:
    strength = "Exceptional"

print("Strength:", strength)

print("\nSuggestions:")

if length < 12:
    print("- Use at least 12 characters.")

if not has_upper:
    print("- Add uppercase letters.")

if not has_lower:
    print("- Add lowercase letters.")

if not has_digit:
    print("- Include numbers.")

if not has_special:
    print("- Include special characters.")

if is_common:
    print("- Avoid common passwords.")

    
