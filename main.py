# Build a tool that assesses the strength of a password based on criteria such as length, 
# presence of uppercase and lowercase letters, numbers, and special characters. 
# Provide Feedback to users on the password's strength.
import re

def passwordChecker(password):
    score = 0
    if (len(password) < 8):
        return 0
    else:
        score += 1

    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search("[!@#$%&*()-_=+]", password):
        score += 1

    return score


def main():
    password = input("Enter Password\n")
    score = passwordChecker(password)
    message = ''
    if(score == 0):
        message = f"Password too short. It should atleast contains 8 characters. Your Contains {len(password)}."
    
    if score < 2:
        message = 'Password Strength: WEAK'
    elif score < 4:
        message = 'Password Strength: MODERATE'
    else:
        message = 'Password Strength: STRONG'

    print(message)


if __name__ == "__main__":
    main()